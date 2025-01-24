
# This file was generated by generate.py. Do not modify directly.
from sys import audit
from types import TracebackType  # noqa:F401
from typing import Optional, Any, Callable, Dict, List, Union, Text, Tuple, TypeVar, Type  # noqa:F401
import importlib.metadata
__version__ = importlib.metadata.version('dd_trace_api')


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
    

class Span():
    
    
    def __enter__(self) -> 'Span':
        audit(_DD_HOOK_PREFIX + "Span.__enter__", ([], {}))
        return self
        
    
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.__exit__", ([exc_type, exc_val, exc_tb], {}))
        return None
        
    
    def set_exc_info(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_exc_info", ([exc_type, exc_val, exc_tb], {}))
        return None
        
    
    def set_link(self, trace_id: int, span_id: int, tracestate:Optional[str]=None, flags:Optional[int]=None, attributes:Optional[Dict[str, Any]]=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_link", ([trace_id, span_id], {'tracestate': tracestate, 'flags': flags, 'attributes': attributes}))
        return None
        
    
    def link_span(self, attributes:Optional[Dict[str, Any]]=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.link_span", ([], {'attributes': attributes}))
        return None
        
    
    def set_traceback(self, limit: Optional[int]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_traceback", ([limit], {}))
        return None
        
    
    def set_tags(self, tags: Dict[_TagNameType, Any]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tags", ([tags], {}))
        return None
        
    
    def set_tag_str(self, key: _TagNameType, value: Text) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tag_str", ([key, value], {}))
        return None
        
    
    def set_struct_tag(self, key: str, value: Dict[str, Any]) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_struct_tag", ([key, value], {}))
        return None
        
    
    def finish_with_ancestors(self) -> None:
        audit(_DD_HOOK_PREFIX + "Span.finish_with_ancestors", ([], {}))
        return None
        
    
    def finish(self, finish_time:Optional[float]=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.finish", ([], {'finish_time': finish_time}))
        return None
        
    
    def set_tag(self, key: _TagNameType, value:Any=None) -> None:
        audit(_DD_HOOK_PREFIX + "Span.set_tag", ([key], {'value': value}))
        return None
        
    

class data_streams():
    
    
    def set_consume_checkpoint(self, typ: str, source: str, carrier_get: Callable) -> None:
        audit(_DD_HOOK_PREFIX + "data_streams.set_consume_checkpoint", ([typ, source, carrier_get], {}))
        return None
        
    
    def set_produce_checkpoint(self, typ: str, target: str, carrier_set: Callable) -> None:
        audit(_DD_HOOK_PREFIX + "data_streams.set_produce_checkpoint", ([typ, target, carrier_set], {}))
        return None
        
    

class HTTPPropagator():
    
    @staticmethod
    def inject(span_context: _Context, headers: Dict[str, str], non_active_span:Optional[Span]=None) -> None:
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.inject", ([span_context, headers], {'non_active_span': non_active_span}))
        return None
        
    @staticmethod
    def extract(headers: Any) -> None:
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.extract", ([headers], {}))
        return None
        
    

http = _Stub()

setattr(http, "HTTPPropagator", HTTPPropagator)
    
    

class Tracer():
    
    
    def flush(self) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.flush", ([], {}))
        return None
        
    
    def set_tags(self, tags: Dict[str, str]) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.set_tags", ([tags], {}))
        return None
        
    
    def shutdown(self, timeout: Optional[float]) -> None:
        audit(_DD_HOOK_PREFIX + "Tracer.shutdown", ([timeout], {}))
        return None
        
    
    def start_span(self, name: str, child_of:Optional[Union[Span, _Context]]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None, activate:bool='False') -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.start_span", ([name], {'child_of': child_of, 'service': service, 'resource': resource, 'span_type': span_type, 'activate': activate}))
        return Span()
        
    
    def current_root_span(self) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.current_root_span", ([], {}))
        return Span()
        
    
    def current_span(self) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.current_span", ([], {}))
        return Span()
        
    
    def trace(self, name: str, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Span:
        audit(_DD_HOOK_PREFIX + "Tracer.trace", ([name], {'service': service, 'resource': resource, 'span_type': span_type}))
        return Span()
        
    
    def wrap(self, name:Optional[str]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Callable[[AnyCallable], AnyCallable]:
        audit(_DD_HOOK_PREFIX + "Tracer.wrap", ([], {'name': name, 'service': service, 'resource': resource, 'span_type': span_type}))
        return lambda *args, **kwargs: None
        
    

class Pin():
    
    
    def onto(self, obj: Any, send:bool=True) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.onto", ([obj], {'send': send}))
        return None
        
    
    def remove_from(self, obj: Any) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.remove_from", ([obj], {}))
        return None
        
    
    def clone(self, service:Optional[str]=None, tags:Optional[Dict[str, str]]=None, tracer:Tracer=None) -> None:
        audit(_DD_HOOK_PREFIX + "Pin.clone", ([], {'service': service, 'tags': tags, 'tracer': tracer}))
        return None
        
    

propagation = _Stub()

setattr(propagation, "http", http)
    
    

tracer = _Stub()

setattr(tracer, "Tracer", Tracer)
    
    

pin = _Stub()

setattr(pin, "Pin", Pin)
    
    

span = _Stub()

setattr(span, "Span", Span)
    
    
