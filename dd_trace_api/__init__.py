
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
    

class Context():
    
    
    def set_baggage_item(self) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Context.set_baggage_item", ([shared_state], {}))
        return retval
        
    

class Span():
    
    
    def __enter__(self) -> 'Span':
        
        retval = self
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.__enter__", ([shared_state], {}))
        return retval
        
    
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.__exit__", ([shared_state, exc_type, exc_val, exc_tb], {}))
        return retval
        
    
    def set_exc_info(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_exc_info", ([shared_state, exc_type, exc_val, exc_tb], {}))
        return retval
        
    
    def set_link(self, trace_id: int, span_id: int, tracestate:Optional[str]=None, flags:Optional[int]=None, attributes:Optional[Dict[str, Any]]=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_link", ([shared_state, trace_id, span_id], {'tracestate': tracestate, 'flags': flags, 'attributes': attributes}))
        return retval
        
    
    def link_span(self, context: Context, attributes:Optional[Dict[str, Any]]=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.link_span", ([shared_state, context], {'attributes': attributes}))
        return retval
        
    
    def set_traceback(self, limit:Optional[int]=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_traceback", ([shared_state], {'limit': limit}))
        return retval
        
    
    def set_tags(self, tags: Dict[Union[Text, bytes], Any]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_tags", ([shared_state, tags], {}))
        return retval
        
    
    def set_tag_str(self, key: Union[Text, bytes], value: Text) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_tag_str", ([shared_state, key, value], {}))
        return retval
        
    
    def set_struct_tag(self, key: str, value: Dict[str, Any]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_struct_tag", ([shared_state, key, value], {}))
        return retval
        
    
    def finish_with_ancestors(self) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.finish_with_ancestors", ([shared_state], {}))
        return retval
        
    
    def finish(self, finish_time:Optional[float]=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.finish", ([shared_state], {'finish_time': finish_time}))
        return retval
        
    
    def set_tag(self, key: Union[Text, bytes], value:Any=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval, 'stub_self': self}
        audit(_DD_HOOK_PREFIX + "Span.set_tag", ([shared_state, key], {'value': value}))
        return retval
        
    

class data_streams():
    
    
    def set_consume_checkpoint(self, typ: str, source: str, carrier_get: Callable) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "data_streams.set_consume_checkpoint", ([shared_state, typ, source, carrier_get], {}))
        return retval
        
    
    def set_produce_checkpoint(self, typ: str, target: str, carrier_set: Callable) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "data_streams.set_produce_checkpoint", ([shared_state, typ, target, carrier_set], {}))
        return retval
        
    

class HTTPPropagator():
    
    @staticmethod
    def inject(span_context: Context, headers: Dict[str, str], non_active_span:Optional[Span]=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.inject", ([shared_state, span_context, headers], {'non_active_span': non_active_span}))
        return retval
        
    @staticmethod
    def extract(headers: Any) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "HTTPPropagator.extract", ([shared_state, headers], {}))
        return retval
        
    

http = _Stub()

setattr(http, "HTTPPropagator", HTTPPropagator)
    
    

class TraceFilter():
    
    
    def process_trace(self, trace: List[Span]) -> Optional[List[Span]]:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "TraceFilter.process_trace", ([shared_state, trace], {}))
        return retval
        
    

class Tracer():
    
    
    def flush(self) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.flush", ([shared_state], {}))
        return retval
        
    
    def set_tags(self, tags: Dict[str, str]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.set_tags", ([shared_state, tags], {}))
        return retval
        
    
    def shutdown(self, timeout: Optional[float]) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.shutdown", ([shared_state, timeout], {}))
        return retval
        
    
    def start_span(self, name: str, child_of:Optional[Union[Span, Context]]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None, activate:bool='False') -> Span:
        
        retval = Span()
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.start_span", ([shared_state, name], {'child_of': child_of, 'service': service, 'resource': resource, 'span_type': span_type, 'activate': activate}))
        return retval
        
    
    def current_root_span(self) -> Span:
        
        retval = Span()
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.current_root_span", ([shared_state], {}))
        return retval
        
    
    def current_span(self) -> Span:
        
        retval = Span()
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.current_span", ([shared_state], {}))
        return retval
        
    
    def trace(self, name: str, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Span:
        
        retval = Span()
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.trace", ([shared_state, name], {'service': service, 'resource': resource, 'span_type': span_type}))
        return retval
        
    
    def wrap(self, name:Optional[str]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Callable[[TypeVar('AnyCallable', bound=Callable)], TypeVar('AnyCallable', bound=Callable)]:
        
        def wrap_decorator(f):
            @functools.wraps(f)
            def func_wrapper(*args, **kwargs):
                return f(*args, **kwargs)

            return func_wrapper
    
        retval = wrap_decorator
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Tracer.wrap", ([shared_state], {'name': name, 'service': service, 'resource': resource, 'span_type': span_type}))
        return retval
        
    

class Pin():
    
    
    def onto(self, obj: Any, send:bool=True) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Pin.onto", ([shared_state, obj], {'send': send}))
        return retval
        
    
    def remove_from(self, obj: Any) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Pin.remove_from", ([shared_state, obj], {}))
        return retval
        
    
    def clone(self, service:Optional[str]=None, tags:Optional[Dict[str, str]]=None, tracer:Tracer=None) -> None:
        
        retval = None
        shared_state = {'api_return_value': retval}
        audit(_DD_HOOK_PREFIX + "Pin.clone", ([shared_state], {'service': service, 'tags': tags, 'tracer': tracer}))
        return retval
        
    

propagation = _Stub()

setattr(propagation, "http", http)
    
    

tracer = Tracer()

    

pin = _Stub()

setattr(pin, "Pin", Pin)
    
    

context = _Stub()

setattr(context, "Context", Context)
    
    

span = _Stub()

setattr(span, "Span", Span)
    
    
