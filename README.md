# Advent of Code

[![Build Status](https://travis-ci.com/pozole-rojo/advent-of-code-2020.svg?branch=main)](https://travis-ci.com/pozole-rojo/advent-of-code-2020)
[![codecov](https://codecov.io/gh/pozole-rojo/advent-of-code-2020/branch/main/graph/badge.svg?token=FRKAQ6KEWB)](https://codecov.io/gh/pozole-rojo/advent-of-code-2020)

Here are my solutions for the [Advent of Code puzzles](https://adventofcode.com). The goal is to solve these problems using TDD in Python.

## Requirements

 1. Python 3
 2. Virtual Environment

## Setup

Spin up the virtual environment and activate it to install the required python packages.

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

#maybe required
chmod 755 run_linter.sh
```

## Running Workflow

The repository is setup with `pylint` and `black` so the Travis CI will check that the repository is perfectly formatted and has no linting issues.
I have created `run_linter.sh` to run the checks for `pylint` and `black` with one command.

### Running linter

```bash
./run_linter.sh

#if you get any formatting failures run the following
black .
```

### Running the tests

I have setup the repo for doing unit testing as well as integration testing.

The unit tests should prove out the functionality of feature by providing different small sample data,
while the integration tests are expected to prove out the full solution of the feature by using the sample input data that
is provided by the puzzle description.

Running the tests

```bash
#Unit tests only
pytest tests/unit/

#Integration tests only
pytest tests/integration/

#All tests
pytest
```
