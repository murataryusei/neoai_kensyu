.PHONY: tests
tests: ## run tests with poetry (isort, black, pflake8, mypy)
	@echo "🚀 Launching the tests..."
	poetry run black .
	poetry run isort .
	poetry run pflake8 .
	poetry run mypy .
	@echo "\033[33;45mAll tests passed! ✨🍾🥳🍾✨\033[0m"


.PHONY: tests_strict
tests_strict: ## run tests with poetry (isort, black, pflake8, mypy)
	@echo "🚀 Launching the strict tests..."
	poetry run isort .
	poetry run black .
	poetry run pflake8 .
	poetry run mypy . --strict
	@echo "\033[33;45mAll strict tests passed! ✨🍾🤩🍾✨\033[0m"