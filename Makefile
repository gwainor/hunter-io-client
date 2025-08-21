## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## lint-check - Run linters
lint-check:
	uv run flake8 app tests

## type-check - Run type checkers
type-check:
	uv run mypy app tests

## fix-imports - Fix import order
fix-imports:
	uv run isort app tests

## code-check - Run all checks
code-check: fix-imports lint-check type-check

## test - Run all tests
test:
	uv run pytest
