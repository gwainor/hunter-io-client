# Simple Hunter IO API client

This project is an experiment on [hunter.io](https://hunter.io) API service.

You can find person information using domain and person's first and last name.

## Installation

The project uses [uv](https://docs.astral.sh/uv/) package manager.
To install dependencies run the following command:

```sh
uv sync
```

## Usage

Update the `app/main.py` with the necessary information and run following command:

```sh
uv run -m test
```

## Checking lint, type, and format errors

There are several commands can be run. Type `make` in terminal for all of them.

To run the all commands at once, run the following command:

```sh
make code-check
```

It will run `isort` first, then `flake8`, and at last `mypy`.

## Running tests

Ensure your `.env` file is there.

Run following command for tests:

```sh
make test
```

Code coverage: 100%
