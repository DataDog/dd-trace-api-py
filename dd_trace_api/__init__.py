from sys import audit, addaudithook
from typing import Type, Optional


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

    def _define(self, name, instance):
        instance._public_name = name
        instance._attribute_of = self.__class__.__name__
        setattr(self, name, instance)


class _CallableStub(_Stub):
    def __init__(self, return_type: Optional[Type] = None, *args):
        super(_CallableStub, self).__init__(*args)
        self.return_type = return_type or _Stub

    def __call__(self, *args, **kwargs):
        audit(f"{_DD_HOOK_PREFIX}{self._attribute_of or '_Stub'}.{self._public_name or 'foo'}")
        return self.return_type() or None


_SpanStub_attributes = {}


class _SpanStub(_Stub):
    def __init__(self):
        super(_SpanStub, self).__init__()
        self.name = _Stub()
        self.service = _Stub()
        self.span_type = _Stub()
        self.error = _Stub()
        self.start_ms = _Stub()
        self.duration_ms = _Stub()
        self.span_id = _Stub()
        self.parent_id = _Stub()
        self._define("start", _CallableStub())
        self.resource = _Stub()
        self.finished = _Stub()
        self.duration = _Stub()
        self.sampled = _Stub()
        self._define("finish", _CallableStub())
        self._define("set_tag", _CallableStub())
        self._define("set_struct_tag", _CallableStub())
        self._define("get_struct_tag", _CallableStub())
        self._define("set_tag_str", _CallableStub())
        self._define("get_tag", _CallableStub())
        self._define("get_tags", _CallableStub())
        self._define("set_tags", _CallableStub())
        self._define("set_metric", _CallableStub())
        self._define("set_metrics", _CallableStub())
        self._define("get_metric", _CallableStub())
        self._define("get_metrics", _CallableStub())
        self._define("set_traceback", _CallableStub())
        self._define("set_exc_info", _CallableStub())
        self.context = _Stub()
        self._define("link_span", _CallableStub())
        self._define("set_link", _CallableStub())
        self._define("finish_with_ancestors", _CallableStub())


class Span(_SpanStub):
    pass


class Tracer(_Stub):
    def __init__(self):
        self._define("sample", _CallableStub())
        self.sampler = _Stub()
        self._define("on_start_span", _CallableStub())
        self._define("deregister_on_start_span", _CallableStub())
        self.debug_logging = _Stub()
        self.current_trace_context = _Stub()
        self._define("get_log_correlation_context", _CallableStub())
        self._define("start_span", _CallableStub(_SpanStub))
        self._define("trace", _CallableStub())
        self._define("current_root_span", _CallableStub(_SpanStub))
        self._define("current_span", _CallableStub(_SpanStub))
        self.agent_trace_url = _Stub()
        self._define("flush", _CallableStub())
        self._define("wrap", _CallableStub())
        self._define("set_tags", _CallableStub())
        self._define("shutdown", _CallableStub())
        self.enabled = _Stub()
        self.context_provider = _Stub()


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
