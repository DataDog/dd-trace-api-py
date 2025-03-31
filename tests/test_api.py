import os
from sys import addaudithook

import pytest
import yaml

import ddtrace_api


with open(os.path.join(os.path.dirname(__file__), "..", "api.yaml")) as definition_stream:
    definition = yaml.safe_load(definition_stream)


_DD_HOOK_PREFIX = "dd.hooks."


def _hook(name, args):
    if name.startswith(_DD_HOOK_PREFIX):
        print(f"Triggered hook with name {name}")


addaudithook(_hook)


def _traverse(node, obj_under_test):
    for node_name, node_data in node.get("attributes", node.get("methods", {})).items():
        try:
            _attribute = getattr(obj_under_test, node_name)
        except AttributeError:
            _attribute = getattr(obj_under_test(), node_name)
        if "methods" in node_data:
            for method_name, method_info in node_data["methods"].items():
                posargs_count = len(method_info.get("posargs", {}))
                kwargs = {k: None for k in method_info.get("kwargs", {}).keys()}
                posargs = [] + [None] * posargs_count
                if not method_info.get("static", False):
                    try:
                        callee = _attribute()
                    except TypeError:
                        callee = _attribute
                else:
                    callee = _attribute
                with pytest.raises(TypeError):
                    if posargs_count > 0:
                        getattr(callee, method_name)(*posargs[:-1])
                    else:
                        getattr(callee, method_name)(*([None] * len(kwargs) + 1))
                getattr(callee, method_name)(*posargs, **kwargs)
        if "attributes" in node_data or "methods" in node_data:
            _traverse(node_data, _attribute)


def test_api_accessible():
    _traverse(definition, ddtrace_api)


def test_wrap():
    @ddtrace_api.tracer.wrap()
    def foo():
        return 1

    result = foo()
    assert result == 1
