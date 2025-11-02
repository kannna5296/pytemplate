# devcontainer上で実行する前提
format:
	poetry run ruff format .

lint:
	poetry run ruff check --fix .
