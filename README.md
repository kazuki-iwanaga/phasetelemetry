> [!WARNING]
> Currently under development.

# PhaseTelemetry

PhaseTelemetry is an instrumentation library compatible with both Python 2.7 and 3.x. Please note that our implementation is heavily influenced by the OpenTelemetry Python SDK and therefore inherits its Apache 2.0 license.

# Getting Started

## Installation

```bash
pip install git+https://github.com/kazuki-iwanaga/phasetelemetry.git@v0.1.0
```
or
```bash
uv add git+https://github.com/kazuki-iwanaga/phasetelemetry.git@v0.1.0
```

## Usage
TODO

# Development

## Setup

Use Visual Studio Code Dev Containers; otherwise, refer to the configuration files (e.g., `.devcontainer/compose.yaml`) and set up your environment by yourself.

## Tools

Use `tox` to run formatting, linting and tests across multiple Python versions (2.7 and 3.11).

```bash
tox -e format  # Run yapf and isort
tox -e lint    # Run flake8
tox run        # Run pytest
```

We also provide some `make` commands:

```bash
make format  # Run `tox -e format`
make fmt     # (Same as above)
make lint    # Run `tox -e lint`
make test    # Run `tox run`
```
