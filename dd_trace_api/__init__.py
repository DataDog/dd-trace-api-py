class Tracer:
    __slots__ = [
        "sample",
        "sampler",
        "on_start_span",
        "deregister_on_start_span",
        "debug_logging",
        "current_trace_context",
        "get_log_correlation_context",
        "configure",
        "start_span",
        "trace",
        "current_root_span",
        "current_span",
        "agent_trace_url",
        "flush",
        "wrap",
        "set_tags",
        "shutdown",
        "enabled",
        "context_provider",
    ]


class Span:
    __slots__ = [
        "name",
        "service",
        "span_type",
        "error",
        "start_ms",
        "duration_ms",
        "span_id",
        "parent_id",
        "start",
        "resource",
        "finished",
        "duration",
        "sampled",
        "finish",
        "set_tag",
        "set_struct_tag",
        "get_struct_tag",
        "set_tag_str",
        "get_tag",
        "get_tags",
        "set_tags",
        "set_metric",
        "set_metrics",
        "get_metric",
        "get_metrics",
        "set_traceback",
        "set_exc_info",
        "context",
        "link_span",
        "set_link",
        "finish_with_ancestors",
    ]


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


class tracer:
    __slots__ = ["Tracer"]
