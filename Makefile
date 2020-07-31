install:
	@poetry install

selfcheck:
	poetry check

lint:
	poetry run flake8 gendiff

check: selfcheck lint

build: check
	@poetry build

publish: build
	poetry publish -r testpypi

.PHONY: install lint selfcheck check build
