.PHONY: format fmt
format fmt:
	@tox -e format

.PHONY: test
test:
	@tox run-parallel
