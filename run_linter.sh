#!/bin/bash
pylint aoc
pylint tests/unit
pylint tests/integration

black --check .


