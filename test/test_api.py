import os

import pytest
import yaml

import dd_trace_api

with open(os.path.join(os.path.dirname(dd_trace_api.__file__), "api.yaml")) as definition_stream:
    definition = yaml.safe_load(definition_stream)


def _traverse(node, obj_under_test):
    print(f"obj: {obj_under_test.__class__.__name__}")
    for node_name, node_data in node.get("attributes", node.get("methods", {})).items():
        print(f"node name: {node_name}")
        print(f"node data: {node_data}")
        try:
            _attribute = getattr(obj_under_test, node_name)
        except AttributeError:
            _attribute = getattr(obj_under_test(), node_name)
        if "methods" in node_data:
            for method_name, method_info in node_data["methods"].items():
                posargs_count = len(method_info.get("posargs", {}))
                kwargs = {k: None for k in method_info.get("kwargs", {}).keys()}
                posargs = [] + [None] * posargs_count
                print(f"method: {method_info}")
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
    _traverse(definition, dd_trace_api)
    for attr_name, attr_info in definition["attributes"].items():
        assert attr_name in dd_trace_api.__all__
