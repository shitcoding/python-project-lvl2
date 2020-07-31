install:
	@poetry install

test:
	poetry run pytest gendiff tests

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	@poetry build

publish: build
	poetry publish -r testpypi

.PHONY: install test lint selfcheck check build publish
