# devcontainer上で実行する前提
.PHONY: format lint test

format:
	poetry run ruff format .

lint:
	poetry run ruff check --fix .

test:
	poetry run python src/test/test_feed.py
