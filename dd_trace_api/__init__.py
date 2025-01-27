
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
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.__enter__", ([shared_state], {}))
        retval = self
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.__exit__", ([shared_state, exc_type, exc_val, exc_tb], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_exc_info(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_exc_info", ([shared_state, exc_type, exc_val, exc_tb], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_link(self, trace_id: int, span_id: int, tracestate:Optional[str]=None, flags:Optional[int]=None, attributes:Optional[Dict[str, Any]]=None) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_link", ([shared_state, trace_id, span_id], {'tracestate': tracestate, 'flags': flags, 'attributes': attributes}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def link_span(self, attributes:Optional[Dict[str, Any]]=None) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.link_span", ([shared_state], {'attributes': attributes}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_traceback(self, limit: Optional[int]) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_traceback", ([shared_state, limit], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_tags(self, tags: Dict[_TagNameType, Any]) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_tags", ([shared_state, tags], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_tag_str(self, key: _TagNameType, value: Text) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_tag_str", ([shared_state, key, value], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_struct_tag(self, key: str, value: Dict[str, Any]) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_struct_tag", ([shared_state, key, value], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def finish_with_ancestors(self) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.finish_with_ancestors", ([shared_state], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def finish(self, finish_time:Optional[float]=None) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.finish", ([shared_state], {'finish_time': finish_time}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_tag(self, key: _TagNameType, value:Any=None) -> None:
        shared_state = {"stub_self": self}
        audit(_DD_HOOK_PREFIX + "Span.set_tag", ([shared_state, key], {'value': value}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    

class data_streams():
    
    
    def set_consume_checkpoint(self, typ: str, source: str, carrier_get: Callable) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "data_streams.set_consume_checkpoint", ([shared_state, typ, source, carrier_get], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_produce_checkpoint(self, typ: str, target: str, carrier_set: Callable) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "data_streams.set_produce_checkpoint", ([shared_state, typ, target, carrier_set], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    

class HTTPPropagator():
    
    @staticmethod
    def inject(span_context: _Context, headers: Dict[str, str], non_active_span:Optional[Span]=None) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.inject", ([shared_state, span_context, headers], {'non_active_span': non_active_span}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    @staticmethod
    def extract(headers: Any) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.extract", ([shared_state, headers], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    

http = _Stub()

setattr(http, "HTTPPropagator", HTTPPropagator)
    
    

class Tracer():
    
    
    def flush(self) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.flush", ([shared_state], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def set_tags(self, tags: Dict[str, str]) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.set_tags", ([shared_state, tags], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def shutdown(self, timeout: Optional[float]) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.shutdown", ([shared_state, timeout], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def start_span(self, name: str, child_of:Optional[Union[Span, _Context]]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None, activate:bool='False') -> Span:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.start_span", ([shared_state, name], {'child_of': child_of, 'service': service, 'resource': resource, 'span_type': span_type, 'activate': activate}))
        retval = Span()
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def current_root_span(self) -> Span:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.current_root_span", ([shared_state], {}))
        retval = Span()
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def current_span(self) -> Span:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.current_span", ([shared_state], {}))
        retval = Span()
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def trace(self, name: str, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Span:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.trace", ([shared_state, name], {'service': service, 'resource': resource, 'span_type': span_type}))
        retval = Span()
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def wrap(self, name:Optional[str]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Callable[[AnyCallable], AnyCallable]:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Tracer.wrap", ([shared_state], {'name': name, 'service': service, 'resource': resource, 'span_type': span_type}))
        retval = lambda *args, **kwargs: None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    

class Pin():
    
    
    def onto(self, obj: Any, send:bool=True) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Pin.onto", ([shared_state, obj], {'send': send}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def remove_from(self, obj: Any) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Pin.remove_from", ([shared_state, obj], {}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    
    def clone(self, service:Optional[str]=None, tags:Optional[Dict[str, str]]=None, tracer:Tracer=None) -> None:
        shared_state = {}
        audit(_DD_HOOK_PREFIX + "Pin.clone", ([shared_state], {'service': service, 'tags': tags, 'tracer': tracer}))
        retval = None
        if retval is not None:
            for key, value in shared_state.items():
                if value is not self:
                    setattr(retval, "_" + key, value)
        return retval
        
    

propagation = _Stub()

setattr(propagation, "http", http)
    
    

tracer = _Stub()

setattr(tracer, "Tracer", Tracer)
    
    

pin = _Stub()

setattr(pin, "Pin", Pin)
    
    

span = _Stub()

setattr(span, "Span", Span)
    
    
