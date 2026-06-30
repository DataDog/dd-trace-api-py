dd-trace-api-py
===============

This library implements a public Python API used to write custom instrumentation code for Datadog [Distributed Tracing](https://docs.datadoghq.com/tracing/).
This library does not implement any of the functionality powering the tracing product, it **ONLY** implements the public API.
You can write Python code against this API and its semantic versioning, but the API calls will be no-ops if you haven't
performed the [manual instrumentation setup process](https://ddtrace.readthedocs.io/en/stable/installation_quickstart.html#tracing).

If you want to use Datadog tracing and don't have a specific need to write your own instrumentation, you should use
[single-step instrumentation](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/single-step-apm/?tab=linuxhostorvm#enabling-apm-on-your-applications),
which doesn't involve this library.

To make your first contribution to this library, see [the contributing docs](https://github.com/DataDog/dd-trace-api-py/blob/main/docs/contributing.md).
