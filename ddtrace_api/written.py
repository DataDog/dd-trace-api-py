import functools
from typing import Optional, Callable, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from mypy_extensions import VarArg, KwArg  # noqa
    from typing import Any  # noqa

AnyCallable = TypeVar("AnyCallable", bound=Callable)


def _Tracer_wrap(
    self,  # this will be bound to a Tracer instance
    name: Optional[str] = None,
    service: Optional[str] = None,
    resource: Optional[str] = None,
    span_type: Optional[str] = None,
):
    # type: (...) -> Callable[[VarArg(Any), KwArg(Any)], Any]
    """
    A function returning a decorator used to trace an entire function. If the traced function
    is a coroutine, it traces the coroutine execution when is awaited.
    If a ``wrap_executor`` callable has been provided in the ``Tracer.configure()``
    method, it will be called instead of the default one when the function
    decorator is invoked.

    >>> @tracer.wrap("my.wrapped.function", service="my.service")
        def run():
            return "run"

    >>> # name will default to "execute" if unset
        @tracer.wrap()
        def execute():
            return "executed"

    >>> # or use it in asyncio coroutines
        @tracer.wrap()
        async def coroutine():
            return "executed"

    >>> @tracer.wrap()
        @asyncio.coroutine
        def coroutine():
            return "executed"

    You can access the current span using `tracer.current_span()` to set
    tags:

    >>> @tracer.wrap()
        def execute():
            span = tracer.current_span()
            span.set_tag("a", "b")
    """

    def wrap_decorator(f: AnyCallable):
        # type: (...) -> Callable[[VarArg(Any), KwArg(Any)], Any]
        @functools.wraps(f)
        def func_wrapper(*args, **kwargs):
            with self.trace(
                name or "%s.%s" % (f.__module__, f.__name__),
                service=service,
                resource=resource,
                span_type=span_type,
            ):
                return f(*args, **kwargs)

        return func_wrapper

    return wrap_decorator
