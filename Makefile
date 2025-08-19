lint-check:
	uv run flake8 app

type-check:
	uv run mypy app

fix-imports:
	uv run isort app

code-check: fix-imports lint-check type-check
