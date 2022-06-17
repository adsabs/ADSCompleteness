# ADSCompleteness

<p align="center">

![CI Status](https://github.com/adsabs/ADSCompleteness/actions/workflows/ci.yml/badge.svg)

  <!--
  <a href="https://codecov.io/gh/adsabs/ADSCompleteness">
    <img src="https://img.shields.io/codecov/c/github/adsabs/ADSCompleteness.svg?logo=codecov&logoColor=fff&style=flat-square" alt="Test coverage percentage">
  </a>
  //-->
</p>

Generate and update coverage completeness statistics for ADS Journals

## Installation

Install this via pip (or your favourite package manager):

```bash
pip install ADSCompleteness
```

## Development

Install locally into virtualenv

```bash
virtualenv .venv
source .venv/bin/activate
pip install .[dev]
pip install .
pre-commit install
pre-commit install --hook-type commit-msg
```



## Documentation

[documentation](https://ADSCompleteness.readthedocs.io)
