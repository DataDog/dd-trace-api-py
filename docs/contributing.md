Contributing
============

Set up your local environment with

```
$ pip install -e '.[dev]'
```

Generating the Code
-------------------

Most of this package's API is defined declaratively in `api.yml`. This file is the source of truth
used by the code generation logic in `generate.py`. To update the code based on changes to `api.yml`, run

```
$ hatch run generate:api
```

Testing
-------

Run the test suite with

```
$ hatch run test:test
```

Release notes
-------------

Release notes are managed by `reno <https://docs.openstack.org/reno/latest/>`_.
To create a new release note::

```
$ hatch run release:notes <slug>
```

where `<slug>` is a short identifier for the change. Then edit the new file to include details about the change.
