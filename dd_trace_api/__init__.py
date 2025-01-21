
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
    

class data_streams():
    
    
    def set_consume_checkpoint(self, typ: str, source: str, carrier_get: Callable) -> None:
        audit(_DD_HOOK_PREFIX + "data_streams.set_consume_checkpoint")
        return None
        

    
    def set_produce_checkpoint(self, typ: str, target: str, carrier_set: Callable) -> None:
        audit(_DD_HOOK_PREFIX + "data_streams.set_produce_checkpoint")
        return None
        
globals()['data_streams'] = data_streams
    

class HTTPPropagator():
    
    @staticmethod
    def inject(span_context: _Context, headers: Dict[str, str], non_active_span:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.inject")
        return None
        

    @staticmethod
    def extract(headers: Any) -> None:
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.extract")
        return None
        
globals()['HTTPPropagator'] = HTTPPropagator
    

http = _Stub()

setattr(http, "HTTPPropagator", HTTPPropagator)
    
globals()['http'] = http
    

class Pin():
    
    
    def onto(self, obj: Any, send:None=True) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.onto")
        return None
        

    
    def remove_from(self, obj: Any) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.remove_from")
        return None
        

    
    def clone(self, service:None=None, tags:None=None, tracer:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.clone")
        return None
        
globals()['Pin'] = Pin
    

class Span():
    
    
    def set_exc_info(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_exc_info")
        return None
        

    
    def set_link(self, trace_id: int, span_id: int, tracestate:None=None, flags:None=None, attributes:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_link")
        return None
        

    
    def link_span(self, attributes:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.link_span")
        return None
        

    
    def set_traceback(self, limit: Optional[int]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_traceback")
        return None
        

    
    def set_tags(self, tags: Dict[_TagNameType, Any]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tags")
        return None
        

    
    def set_tag_str(self, key: _TagNameType, value: Text) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tag_str")
        return None
        

    
    def set_struct_tag(self, key: str, value: Dict[str, Any]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_struct_tag")
        return None
        

    
    def finish_with_ancestors(self) -> None:
        audit(_DD_HOOK_PREFIX + "Span.finish_with_ancestors")
        return None
        

    
    def finish(self, finish_time:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.finish")
        return None
        

    
    def set_tag(self, key: _TagNameType, value:None=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tag")
        return None
        
globals()['Span'] = Span
    

class Tracer():
    
    
    def flush(self) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.flush")
        return None
        

    
    def set_tags(self, tags: Dict[str, str]) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.set_tags")
        return None
        

    
    def shutdown(self, timeout: Optional[float]) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.shutdown")
        return None
        

    
    def start_span(self, name: str, child_of:None=None, service:None=None, resource:None=None, span_type:None=None, activate:None='False') -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.start_span")
        return Span()
        

    
    def current_root_span(self) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.current_root_span")
        return Span()
        

    
    def current_span(self) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.current_span")
        return Span()
        

    
    def trace(self, name: str, service:None=None, resource:None=None, span_type:None=None) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.trace")
        return Span()
        

    
    def wrap(self, name:None=None, service:None=None, resource:None=None, span_type:None=None) -> Callable[[AnyCallable], AnyCallable]:
        audit(_DD_HOOK_PREFIX + "Tracer.wrap")
        return lambda: None
        
globals()['Tracer'] = Tracer
    

tracer = _Stub()

setattr(tracer, "Tracer", Tracer)
    
globals()['tracer'] = tracer
    

pin = _Stub()

setattr(pin, "Pin", Pin)
    
globals()['pin'] = pin
    

span = _Stub()

setattr(span, "Span", Span)
    
globals()['span'] = span
    

propagation = _Stub()

setattr(propagation, "http", http)
    
globals()['propagation'] = propagation
    
