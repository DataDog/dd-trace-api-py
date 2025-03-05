dd-trace-api-py
===============

This library implements a public Python API used to write custom instrumentation code for Datadog [Distributed Tracing](https://docs.datadoghq.com/tracing/).
This library does not implement any of the functionality powering the tracing product, it **ONLY** implements the public API.
You can write Python code against this API and its semantic versioning, but the API calls will be no-ops if you haven't
performed the [manual instrumentation setup process]().

If you want to use Datadog tracing and don't have a specific need to write your own instrumentation, you should use
[single-step instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/?tab=linuxhostorvm#enabling-apm-on-your-applications),
which doesn't involve this library.

If you're not sure which applies to you, or simply to get started with tracing, check out the
[product documentation][setup docs] or the [glossary][visualization docs].

For advanced usage and configuration information, check out the [library documentation][api docs].

To get started as a contributor, see [the contributing docs](https://ddtrace.readthedocs.io/en/stable/contributing.html) first.

[setup docs]: https://docs.datadoghq.com/tracing/setup/python/
[api docs]: https://docs.datadoghq.com/
[visualization docs]: https://docs.datadoghq.com/tracing/visualization/
