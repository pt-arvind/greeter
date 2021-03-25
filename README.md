# Greeter

App to show how to use and install black mypy and type hinting/dataclasses

## Prerequisites

- have pyenv installed or python 3.7+

## First-Time Setup

```bash

$ pyenv global 3.8.2

$ python -m venv ./venv

$ pip install -r requirements-dev.txt

```

## Formatting

```bash

$ black .

```

## Type-Checking/Linting

```bash

$ mypy main.py # can be used on package too

```
