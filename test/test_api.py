import os

import pytest
import yaml

import dd_trace_api

with open(os.path.join(os.path.dirname(dd_trace_api.__file__), "api.yaml")) as definition_stream:
    definition = yaml.safe_load(definition_stream)


def test_api_accessible():
    for attr_name, attr_info in definition["attributes"].items():
        if "methods" in attr_info:
            _class = getattr(dd_trace_api, attr_name)
            instance = _class()
            for method_name, method_info in attr_info["methods"].items():
                posargs_count = len(method_info.get("posargs", {}))
                kwargs = {k: None for k in method_info.get("kwargs", {}).keys()}
                posargs = [] + [None] * posargs_count
                obj_under_test = _class if method_info.get("static", False) else instance
                with pytest.raises(TypeError):
                    if posargs_count > 0:
                        getattr(obj_under_test, method_name)(*posargs[:-1])
                    else:
                        getattr(obj_under_test, method_name)(*([None] * len(kwargs) + 1))
                getattr(obj_under_test, method_name)(*posargs, **kwargs)
        else:
            # XXX this should be resursive
            assert hasattr(dd_trace_api, attr_name)
