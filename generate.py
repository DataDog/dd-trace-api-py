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
{module_name} = {module_info.get("instance_of", "_Stub")}()
{attrs_code}
    """
    _write_out(code)


def _build_decorator():
    code = """
        def wrap_decorator(f):
            @functools.wraps(f)
            def func_wrapper(*args, **kwargs):
                return f(*args, **kwargs)

            return func_wrapper
    """
    return code


def _generate_class(name, class_info):
    method_lines = []
    shares_self = class_info.get("shares_self", False)
    for method_name, method_info in class_info.get("methods", {}).items():
        is_static = method_info.get("static", False)
        return_info = method_info.get("return_info", {})
        posarg_defs, kwarg_defs, args, kwargs = [], [], [], []
        for arg, info in method_info.get("posargs", {}).items():
            posarg_defs.append(f"{arg}: {info['type']}")
            args.append(arg)
        for kwarg, info in method_info.get("kwargs", {}).items():
            kwarg_defs.append(f"{kwarg}:{info.get('type')}={info.get('default').__repr__()}")
            kwargs.append(kwarg)
        kwargs_str = "{" + ", ".join([f"'{kwarg}': {kwarg}" for kwarg in kwargs]) + "}"
        self_param = ["self"] if not is_static else []
        params = ", ".join(self_param + posarg_defs + kwarg_defs)
        args.insert(0, "shared_state")
        args_str = "[" + ", ".join(args) + "]"
        decorator_setup_str = ""
        if method_info.get("decorator", False):
            decorator_setup_str = _build_decorator()
        shared_state_vars = [("api_return_value", "retval")]
        if shares_self:
            shared_state_vars.append(("stub_self", "self"))
        shared_state_str = "{" + ", ".join([f"'{k}': {v}" for k, v in shared_state_vars]) + "}"
        impl_retval_code = ""
        if method_info.get("uses_impl_retval", False):
            impl_retval_code = "shared_state['impl_return_value'] = None"
        method_lines.append(
            f"""
    {"@staticmethod" if is_static else ""}
    def {method_name}({params}) -> {return_info.get('type')}:
        '''
        {method_info.get("docstring", '')}
        '''
        {decorator_setup_str}
        retval = {return_info.get('value')}
        shared_state = {shared_state_str}
        {impl_retval_code}
        audit(_DD_HOOK_PREFIX + "{name}.{method_name or 'foo'}", ({args_str}, {kwargs_str}))
        return shared_state.get("impl_return_value", retval)
        """
        )
    methods_code = "".join(method_lines)
    code = f"""
class {name}():
    {methods_code or "pass"}
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
        if "instance_of" in member_data:
            modules_to_generate.append((member_name, member_data))
    # this has to happen in a second pass because some of the modules reference generated classes
    for member_name, member_data in modules_to_generate:
        _generate_module(member_name, member_data)


def _generate_header():
    code = """
# This file was generated by generate.py. Do not modify directly.
import functools
from sys import audit
from types import TracebackType  # noqa:F401
from typing import Optional, Any, Callable, Dict, List, Union, Text, Tuple, TypeVar, Type  # noqa:F401
import importlib.metadata
__version__ = importlib.metadata.version('dd_trace_api')

_DD_HOOK_PREFIX = "dd.hooks."


class _Stub:
    pass
    """
    _write_out(code)


def _generate_api(node):
    if os.path.isfile(INITPATH):
        os.remove(INITPATH)
    _generate_header()
    _build_classes(node)


_generate_api(definition)
