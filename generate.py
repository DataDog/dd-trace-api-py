import os

import yaml

INITPATH = os.path.join(os.path.dirname(__file__), "dd_trace_api", "__init__.py")
with open(os.path.join(os.path.dirname(__file__), "api.yaml")) as definition_stream:
    definition = yaml.safe_load(definition_stream)


def _generate_module(module_name, module_info):
    """Generate a stub that is not intended to be instantiated in client code"""
    attrs_code = "\n".join(
        [
            f"""
setattr({module_name}, "{attribute_name}", {attribute_name})
    """
            for attribute_name, attribute_value in module_info.get("attributes", {}).items()
        ]
    )
    code = f"""
{module_name} = _Stub()
{attrs_code}
    """
    _write_out(code)


def _generate_class(name, class_info):
    method_lines = []
    for method_name, method_info in class_info.get("methods", {}).items():
        is_static = method_info.get("static", False)
        return_info = method_info.get("return_info", {})
        posarg_defs = [f"{arg}: {info['type']}" for arg, info in method_info.get("posargs", {}).items()]
        kwarg_defs = [
            f"{arg}:{info.get('type')}={info.get('default').__repr__()}"
            for arg, info in method_info.get("kwargs", {}).items()
        ]
        self_param = ["self"] if not is_static else []
        params = ", ".join(self_param + posarg_defs + kwarg_defs)
        method_lines.append(
            f"""
    {"@staticmethod" if is_static else ""}
    def {method_name}({params}) -> {return_info.get('type')}:
        audit(_DD_HOOK_PREFIX + "{name}.{method_name or 'foo'}")
        return {return_info.get('value')}
        """
        )
    methods_code = "".join(method_lines)
    code = f"""
class {name}():
    {methods_code or "pass"}
{name} = {name}
    """
    _write_out(code)


def _write_out(text: str):
    with open(INITPATH, "a+") as f:
        f.write(text + "\n")


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


def _generate_header():
    code = """
from sys import audit
from types import TracebackType  # noqa:F401
from typing import Optional, Any, Callable, Dict, List, Union, Text, Tuple, TypeVar, Type  # noqa:F401


class _Stub:
    pass


_TagNameType = Union[Text, bytes]
AnyCallable = TypeVar("AnyCallable", bound=Callable)

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

class filters:
    __slots__ = ["TraceFilter", "FilterRequestsOnUrl"]


class provider:
    __slots__ = ["BaseContextProvider", "DatadogContextMixin", "DefaultContextProvider", "CIContextProvider"]


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
    """
    _write_out(code)


def _generate_api(node):
    if os.path.isfile(INITPATH):
        os.remove(INITPATH)
    _generate_header()
    _build_classes(node)


_generate_api(definition)
