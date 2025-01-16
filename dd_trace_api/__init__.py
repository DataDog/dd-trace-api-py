import os
from sys import audit, addaudithook
from typing import Optional, Any, Dict, List, Union, Text, Tuple

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
    "sampling_rule",
    "sampler",
    "span",
    "tracer",
]

_DD_HOOK_PREFIX = "dd.hooks."


def _hook(name, args):
    if name.startswith(_DD_HOOK_PREFIX):
        print(f"Triggered hook with name {name}")


addaudithook(_hook)


class _Stub:
    def __init__(self, name: Optional[str] = None):
        self._public_name = name

        if self._public_name is not None:
            self._build_from_spec(self._public_name)

    def _build_from_spec(self, name):
        for method_name, method_info in definition["classes"][name]["methods"].items():
            print(method_info)
            self._define(
                method_name,
                _CallableStub(
                    posargs=[(name, info["type"]) for name, info in method_info.get("posargs", {}).items()],
                    kwargs={
                        name: (info.get("default", None), info["type"])
                        for name, info in method_info.get("kwargs", {}).items()
                    },
                    return_info=("None", "Any"),
                ),
            )

    def _define(self, name, instance):
        instance._public_name = name
        instance._attribute_of = self.__class__.__name__
        setattr(self, name, instance)


class _CallableStub(_Stub):
    def __init__(
        self,
        return_info: Tuple[str, str] = ("None", "Any"),
        posargs: Optional[List[Tuple[str, str]]] = None,
        kwargs: Optional[Dict[Any, str]] = None,
        *args,
    ):
        super(_CallableStub, self).__init__(*args)
        self.return_info = return_info
        self.posargs = posargs
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        if not hasattr(self, f"_inner_{self._public_name}"):
            posarg_defs = ", " + ", ".join(f"{arg}: {_type}" for arg, _type in self.posargs) if self.posargs else ""
            kwarg_defs = (
                ", " + ", ".join(f"{arg}:{_type}={default.__repr__()}" for arg, (default, _type) in self.kwargs.items())
                if self.kwargs
                else ""
            )
            code = f"""
def _inner_{self._public_name}(self{posarg_defs}{kwarg_defs}) -> {self.return_info[1]}:
    return {self.return_info[0]}

bound_method = _inner_{self._public_name}.__get__(self, self.__class__)
setattr(self, '_inner_{self._public_name}', bound_method)
"""
            exec(code)
        inner_fn = getattr(self, f"_inner_{self._public_name}")
        retval = inner_fn(*args, **kwargs)
        audit(f"{_DD_HOOK_PREFIX}{self._attribute_of or '_Stub'}.{self._public_name or 'foo'}")
        return retval


_SpanStub_attributes = {}


class _SpanStub(_Stub):
    def __init__(self):
        super(_SpanStub, self).__init__("_SpanStub")
        self._define("set_struct_tag", _CallableStub(posargs=[("key", "str"), ("value", "Dict[str, Any]")]))
        self._define("set_tag_str", _CallableStub(posargs=[("key", "_TagNameType"), ("value", "Text")]))
        self._define("set_tags", _CallableStub(posargs=[("tags", "Dict[_TagNameType, Any]")]))
        self._define("set_traceback", _CallableStub(posargs=[("limit", "Optional[int]")]))
        self._define(
            "set_exc_info",
            _CallableStub(
                posargs=[
                    ("exc_type", "Type[BaseException]"),
                    ("exc_val", "BaseException"),
                    ("exc_tb", "Optional[TracebackType]"),
                ]
            ),
        )
        self._define(
            "link_span",
            _CallableStub(posargs=[("context", "context")], kwargs={"attributes": (None, "Optional[Dict[str, Any]]")}),
        )
        self._define(
            "set_link",
            _CallableStub(
                posargs=[("trace_id", "int"), ("span_id", "int")],
                kwargs={
                    "tracestate": (None, "Optional[str]"),
                    "flags": (None, "Optional[int]"),
                    "attributes": (None, "Optional[Dict[str, Any]]"),
                },
            ),
        )
        self._define("finish_with_ancestors", _CallableStub())


class Span(_SpanStub):
    pass


class Tracer(_Stub):
    def __init__(self):
        super(Tracer, self).__init__("Tracer")


class _SamplingRule:
    __slots__ = ["sample_rate", "matches", "tags_match", "check_tags", "sample", "choose_matcher"]


class _SamplingError:
    pass


class _BaseSampler:
    __slots__ = ["sample"]


class _BasePrioritySampler:
    __slots__ = ["update_rate_by_service_sample_rates"]


class _AllSampler:
    __slots__ = ["sample"]


class _RateSampler:
    __slots__ = ["sample", "set_sample_rate"]


class _RateByServiceSampler:
    __slots__ = ["sample", "set_sample_rate", "update_rate_by_service_sample_rates"]


class _DatadogSampler:
    __slots__ = ["default_sample_rate", "limiter", "sample", "update_rate_by_service_sample_rates"]


class _BaseContextProvider:
    __slots__ = ["activate", "active"]


class _DatadogContextMixin:
    __slots__ = ["activate", "active"]


class _DefaultContextProvider:
    __slots__ = ["activate", "active"]


class _CIContextProvider:
    __slots__ = ["activate", "active"]


class Pin:
    __slots__ = ["service", "tags", "tracer", "get_from", "override", "enabled", "onto", "remove_from", "clone"]


class _TraceFilter:
    __slots__ = ["process_trace"]


class _FilterRequestsOnUrl:
    __slots__ = ["process_trace"]


class _Context:
    __slots__ = [
        "sampling_priority",
        "trace_id",
        "span_id",
        "dd_origin",
        "dd_user_id",
        "set_baggage_item",
        "get_baggage_item",
        "get_all_baggage_items",
        "remove_baggage_item",
        "remove_all_baggage_items",
    ]


class context:
    __slots__ = ["Context"]


class data_streams:
    __slots__ = ["set_consume_checkpoint", "set_produce_checkpoint"]


class filters:
    __slots__ = ["TraceFilter", "FilterRequestsOnUrl"]


class pin:
    __slots__ = ["Pin"]


class provider:
    __slots__ = ["BaseContextProvider", "DatadogContextMixin", "DefaultContextProvider", "CIContextProvider"]


class sampler:
    __slots__ = [
        "BaseSampler",
        "BasePrioritySampler",
        "AllSampler",
        "RateSampler",
        "RateByServiceSampler",
        "DatadogSampler",
        "SamplingError",
    ]


class sampling_rule:
    __slots__ = ["SamplingRule"]


class span:
    __slots__ = ["Span"]


tracer = _Stub()
tracer.Tracer = Tracer

# TODO - add API from dd-trace-py/ddtrace/propagation/__init__.py
