# Contributing

If you want to add an issue or pull request, please ensure that the [existing issues](https://github.com/acesseonline/pyreportjasper/issues?utf8=✓&q=) don't already cover your question or contribution.

To get started contributing code to the `pyreportjasper` project:

## Installation

We recommend using [`virtualenv`](https://virtualenv.readthedocs.org/en/latest/) to isolate dependencies for development.
This guide assumes that you have already created and activated a virtualenv for this project.

Ensure that you have the latest version of pip installed:
```
pip install -U pip
```

Clone the repository (alternatively, if you plan on making a pull request and are not in the Mapbox organization, use the [github page](https://github.com/mapbox/mapbox-sdk-py) to create your own fork)
```
git clone git@github.com:acesseonline/pyreportjasper.git
cd pyreportjasper
```

Install the dependency
```
pip install jpype1
```

And finally create a separate branch to begin work
```
git checkout -b my-new-feature
```

## Submitting Pull Requests

Pull requests are welcomed! We'd like to review the design and implementation as early as
possible so please submit the pull request even if it's not 100%.
Let us know the purpose of the change and list the remaining items which need to be
addressed before merging. Finally, PR's should include unit tests and documentation
where appropriate.

A good pull request:

-  Is clear.
-  Works across all supported versions of Python.
-  Follows the existing style of the code base (PEP-8).
-  Has comments included as needed.

-  A test case that demonstrates the previous flaw that now passes with
   the included patch, or demonstrates the newly added feature.
-  If it adds/changes a public API, it must also include documentation
   for those changes.
-  Must be appropriately licensed (GNU GENERAL PUBLIC LICENSE).