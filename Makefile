.PHONY: format fmt
format fmt:
	@tox -e format

.PHONY: lint
lint:
	@tox -e lint

.PHONY: test
test:
	@tox run-parallel
