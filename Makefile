# devcontainer上で実行する前提
format:
	uv run ruff format .

lint:
	uv run ruff check --fix .
