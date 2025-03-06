Contributing
============

Generating the Code
-------------------

Most of this package's API is defined declaratively in `api.yml`. This file is the source of truth
used by the code generation logic in `generate.py`. To update the code based on changes to `api.yml`, run

```
$ python generate.py
```

Testing
-------

Run the test suite with

```
$ pip install -e '.[dev]'
$ pytest
```
