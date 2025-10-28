# devcontainer上で実行する前提
.PHONY: format lint

format:
	poetry run ruff format .

lint:
	poetry run ruff check --fix .
