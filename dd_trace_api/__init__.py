import os
from sys import audit, addaudithook
from types import TracebackType  # noqa:F401
from typing import Optional, Any, Callable, Dict, List, Union, Text, Tuple, Type  # noqa:F401

import yaml

with open(os.path.join(os.path.dirname(__file__), "api.yaml")) as definition_stream:
    definition = yaml.safe_load(definition_stream)

_TagNameType = Union[Text, bytes]


__all__ = [
    "Pin",
    "Span",
    "Tracer",
    "context",
    "data_streams",
    "filters",
    "pin",
    "provider",
    "span",
    "tracer",
    "propagation",
]

_DD_HOOK_PREFIX = "dd.hooks."


def _hook(name, args):
    if name.startswith(_DD_HOOK_PREFIX):
        print(f"Triggered hook with name {name}")


addaudithook(_hook)


class _Stub:
    def __init__(self, name: Optional[str] = None):
        self._public_name = name
        self._build_from_spec(self.__class__.__name__)

    def _build_from_spec(self, name):
        if name not in definition["attributes"]:
            return
        for method_name, method_info in definition["attributes"][name]["methods"].items():
            self._define(
                method_name,
                _CallableStub(
                    posargs=[(name, info["type"]) for name, info in method_info.get("posargs", {}).items()],
                    kwargs={
                        name: (info.get("default", None), info["type"])
                        for name, info in method_info.get("kwargs", {}).items()
                    },
                    return_info=("None", "Any"),
                    static=method_info.get("static", False),
                ),
            )

    def _define(self, name, instance):
        instance._public_name = name
        instance._attribute_of = self.__class__.__name__
        setattr(self, name, instance)


def _generate_class(name, class_info):
    static_method_lines = []
    for method_name, method_info in class_info.get("methods", {}).items():
        if not method_info.get("static", False):
            continue
        return_info = method_info.get("return_info", {})
        posarg_defs = [f"{arg}: {info['type']}" for arg, info in method_info.get("posargs", {}).items()]
        kwarg_defs = [
            f"{arg}:{info.get('_type')}={info.get('default').__repr__()}"
            for arg, info in method_info.get("kwargs", {}).items()
        ]
        params = ", ".join(posarg_defs + kwarg_defs)
        method_lines = f"""
    @staticmethod
    def {method_name}({params}) -> {return_info.get('type')}:
        audit("{_DD_HOOK_PREFIX}{name or '_Stub'}.{method_name or 'foo'}")
        return {return_info.get('value')}
        """
        static_method_lines.append(method_lines)
    static_method_code = "\n".join(static_method_lines)
    code = f"""
class {name}(_Stub):
    {static_method_code or "pass"}
globals()['{name}'] = {name}
    """
    exec(code)


def _generate_callable_stub(self):
    if hasattr(self, f"_inner_{self._public_name}"):
        return
    posarg_defs = [f"{arg}: {_type}" for arg, _type in self.posargs]
    kwarg_defs = [f"{arg}:{_type}={default.__repr__()}" for arg, (default, _type) in self.kwargs.items()]
    self_param = ["self" if not self.static else ""]
    params = ", ".join(self_param + posarg_defs + kwarg_defs)
    code = f"""
def _inner_{self._public_name}({params}) -> {self.return_info[1]}:
    return {self.return_info[0]}
"""
    code += f"""
bound_method = _inner_{self._public_name}.__get__(self, self.__class__)
setattr(self, '_inner_{self._public_name}', bound_method)
"""
    exec(code)


class _CallableStub(_Stub):
    def __init__(
        self,
        return_info: Tuple[str, str] = ("None", "Any"),
        posargs: Optional[List[Tuple[str, str]]] = None,
        kwargs: Optional[Dict[Any, str]] = None,
        static: bool = False,
        *args,
    ):
        super(_CallableStub, self).__init__(*args)
        self.return_info = return_info
        self.posargs = posargs
        self.kwargs = kwargs
        self.static = static

    def __call__(self, *args, **kwargs):
        _generate_callable_stub(self)
        inner_fn = getattr(self, f"_inner_{self._public_name}")
        retval = inner_fn(*args, **kwargs)
        audit(f"{_DD_HOOK_PREFIX}{self._attribute_of or '_Stub'}.{self._public_name or 'foo'}")
        return retval


class _BaseContextProvider:
    __slots__ = ["activate", "active"]


class _DatadogContextMixin:
    __slots__ = ["activate", "active"]


class _DefaultContextProvider:
    __slots__ = ["activate", "active"]


class _CIContextProvider:
    __slots__ = ["activate", "active"]


class _TraceFilter:
    __slots__ = ["process_trace"]


class _FilterRequestsOnUrl:
    __slots__ = ["process_trace"]


class _Context:
    __slots__ = [
        "set_baggage_item",
        "remove_baggage_item",
        "remove_all_baggage_items",
    ]


def _generate_module(module_name, module_info):
    """Generate a stub that is not intended to be instantiated in client code"""
    attrs_code = "\n".join(
        [
            f"""
{module_name + "." + attribute_name} = {attribute_name}
    """
            for attribute_name, attribute_value in module_info.get("attributes", {}).items()
        ]
    )
    global_assignment = f"globals()['{module_name}']"
    code = f"""
{module_name} = _Stub()
{attrs_code}
{global_assignment} = {module_name}
    """
    exec(code)


def _iterate_node_members(node):
    for member_info in node.get("attributes", node.get("methods", {})).items():
        yield member_info


def _build_classes(node):
    modules_to_generate = []
    for member_name, member_data in _iterate_node_members(node):
        if "methods" in member_data:
            _generate_class(member_name, member_data)
        if "attributes" in member_data:
            _build_classes(member_data)
            modules_to_generate.append((member_name, member_data))
    # this has to happen in a second pass because some of the modules reference generated classes
    for member_name, member_data in modules_to_generate:
        _generate_module(member_name, member_data)


def _generate_api(node):
    _build_classes(node)


class filters:
    __slots__ = ["TraceFilter", "FilterRequestsOnUrl"]


class provider:
    __slots__ = ["BaseContextProvider", "DatadogContextMixin", "DefaultContextProvider", "CIContextProvider"]


_generate_api(definition)
