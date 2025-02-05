
# This file was generated by generate.py. Do not modify directly.
import functools
from sys import audit
from types import TracebackType  # noqa:F401
from typing import Optional, Any, Callable, Dict, List, Union, Text, Tuple, TypeVar, Type  # noqa:F401
import importlib.metadata
__version__ = importlib.metadata.version('dd_trace_api')

from .constants import _DD_HOOK_NAME
from . import written


class _Stub:
    pass
    

class Span():

    
    def __enter__(self) -> 'Span':
        '''
        
        '''
        retval = self
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, '__enter__'], {}))
        return retval
    
    
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        '''
        
        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, '__exit__', exc_type, exc_val, exc_tb], {}))
        return retval
    
    
    def set_exc_info(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: Optional[TracebackType]) -> None:
        '''
        Tag the span with an error tuple as from ``sys.exc_info()``
        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'set_exc_info', exc_type, exc_val, exc_tb], {}))
        return retval
    
    
    def set_traceback(self, limit:Optional[int]=None) -> None:
        '''
        "If the current stack has an exception, tag the span with the relevant error info. If not, tag
it with the current python stack."

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'set_traceback'], {'limit': limit}))
        return retval
    
    
    def set_tags(self, tags: Dict[Union[Text, bytes], Any]) -> None:
        '''
        Set a dictionary of tags on the given span. Keys and values must be strings (or stringable)
        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'set_tags', tags], {}))
        return retval
    
    
    def finish_with_ancestors(self) -> None:
        '''
        "
Finish this span along with all (accessible) ancestors of this span.

This method is useful if a sudden program shutdown is required and finishing
the trace is desired.
"

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'finish_with_ancestors'], {}))
        return retval
    
    
    def finish(self, finish_time:Optional[float]=None) -> None:
        '''
        "Mark the end time of the span and submit it to the tracer.
If the span has already been finished don't do anything.
"

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'finish'], {'finish_time': finish_time}))
        return retval
    
    

class Tracer():

    
    def flush(self) -> None:
        '''
        "
Flush the tracer's internal buffer, sending spans to Datadog's intake endpoint
"

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'flush'], {}))
        return retval
    
    
    def set_tags(self, tags: Dict[str, str]) -> None:
        '''
        "
Set some tags at the tracer level. This will append those tags to each span created by
the tracer.
"

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'set_tags', tags], {}))
        return retval
    
    
    def shutdown(self, timeout: Optional[float]) -> None:
        '''
        "Shutdown the tracer and flush finished traces. Avoid calling shutdown multiple times."

        '''
        retval = None
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'shutdown', timeout], {}))
        return retval
    
    
    def start_span(self, name: str, child_of:Optional[Span]=None, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None, activate:bool='False') -> Span:
        '''
        'Return a span that represents an operation called ``name``.

Note that the ``.trace`` method will almost always be preferred
over this method as it provides automatic span parenting. This method
should only be used if manual parenting is desired.

To start a new root span::

    span = tracer.start_span("web.request")

To create a child for a root span::

    root_span = tracer.start_span("web.request")
    span = tracer.start_span("web.decoder", child_of=root_span)

Spans from ``start_span`` are not activated by default::

    with tracer.start_span("parent") as parent:
        assert tracer.current_span() is None
        with tracer.start_span("child", child_of=parent):
            assert tracer.current_span() is None

    new_parent = tracer.start_span("new_parent", activate=True)
    assert tracer.current_span() is new_parent
'

        '''
        retval = Span()
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'start_span', name], {'child_of': child_of, 'service': service, 'resource': resource, 'span_type': span_type, 'activate': activate}))
        return retval
    
    
    def current_root_span(self) -> Span:
        '''
        "Returns the local root span of the current execution/process.

Note - This cannot be used to access the true root span of the trace
in a distributed tracing setup if the actual root span occurred in
another execution/process.

This is useful for attaching information to the local root span
of the current execution/process, which is often also service
entry span.

For example::

    # get the local root span
    local_root_span = tracer.current_root_span()
    # set the host just once on the root span
    if local_root_span:
        local_root_span.set_tag('host', '127.0.0.1')
"

        '''
        retval = Span()
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'current_root_span'], {}))
        return retval
    
    
    def current_span(self) -> Span:
        '''
        'Return the active span in the current execution context.

Note that there may be an active span from a distributed trace which will not
be returned by this method.
'

        '''
        retval = Span()
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'current_span'], {}))
        return retval
    
    
    def trace(self, name: str, service:Optional[str]=None, resource:Optional[str]=None, span_type:Optional[str]=None) -> Span:
        '''
        '
Activate and return a new span that inherits from the current active span.

The returned span *must* be ``finish``ed or it will remain in memory
indefinitely::

    >>> span = tracer.trace("web.request")
        try:
            # do something
        finally:
            span.finish()

    >>> with tracer.trace("web.request") as span:
            # do something

Example of the automatic parenting::

    parent = tracer.trace("parent")     # has no parent span
    assert tracer.current_span() is parent

    child  = tracer.trace("child")
    assert child.parent_id == parent.span_id
    assert tracer.current_span() is child
    child.finish()

    # parent is now the active span again
    assert tracer.current_span() is parent
    parent.finish()

    assert tracer.current_span() is None

    parent2 = tracer.trace("parent2")
    assert parent2.parent_id is None
    parent2.finish()
'

        '''
        retval = Span()
        
        # XXX no string concatenation
        audit(_DD_HOOK_NAME, ([retval, self, 'trace', name], {'service': service, 'resource': resource, 'span_type': span_type}))
        return retval
    
    wrap = written._Tracer_wrap
    
    

tracer = Tracer()

    

span = _Stub()

setattr(span, "Span", Span)
    
    
