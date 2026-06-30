Quickstart
==========

All you need to do before you start writing custom Datadog Distributed Tracing instrumentation is install this library:

```
$ pip install ddtrace-api
```

With the library installed, you can import and use it:

```
# example.py

import dd_trace_api
span = dd_trace_api.tracer.start_span("myspan")
span.finish()
```

This code, and anything else you write that correctly uses the API exposed by `dd_trace_api`, will execute without error
and provide valid type information to typecheckers like MyPy. However, it will not actually do anything useful.
Read on to find out how to make it do real stuff.

Making It Work
==============

If you have a piece of code that does `import dd_trace_api` and uses it to instrument for tracing, that instrumentation
doesn't do anything by default. To make it generate and send tracing data to Datadog, it's necessary to install another
package [`ddtrace`](https://github.com/Datadog/dd-trace-py) and bootstrap it at runtime.

```
$ pip install ddtrace
```

With `ddtrace` installed, follow that package's [quickstart instructions](https://ddtrace.readthedocs.io/en/stable/installation_quickstart.html#tracing)
to bootstrap the tracing machinery.

When your code against `dd_trace_api` executes in this context, `ddtrace` will respond to your API calls with
real tracing actions.

How it works
============

When the [`ddtrace`](https://github.com/Datadog/dd-trace-py) package is installed and bootstrapped in a Python
process, it automatically instruments the `ddtrace-api` package. This instrumentation sets up hooks triggered
by the methods of `ddtrace-api`'s public API. Each function call in `ddtrace-api` triggers the corresponding
private functionality in `ddtrace`. For example, when `ddtrace` is active, this code

```
span = dd_trace_api.tracer.start_span("myspan")
```

causes `ddtrace` to create a span called "myspan". A reference to this span is held internally by `ddtrace` and
is not directly accessible via `ddtrace-api`. The object referenced by the `span` name in the code above is a "stub span".
It exposes its part of the public API and proxies calls to those methods to the privately-held "real" `Span` instance.
`ddtrace-api`'s design intention is to make the difference between a stub and a real `Span` irrelevant to the user,
such that you can use a stub like it's a real `Span` and never know the difference. This stub/proxy approach is used for
all classes exposed by `ddtrace-api`.
