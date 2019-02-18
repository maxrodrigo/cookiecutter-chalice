.PHONY: help install clean clean-pyc clean-test test lint run install
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^((?!_)[a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-pyc clean-test ## remove all test, coverage and Python artifacts
	@echo "+ $@"

clean-pyc: ## remove Python file artifacts
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*~' -exec rm -f {} +

clean-test: ## remove test and coverage artifacts
	@rm -f .coverage
	@rm -fr htmlcov/
	@rm -fr .pytest_cache
	@rm -fr .benchmarks

test: clean ## run all, unit and integration tests
	@echo "+ $@"
	@py.test

deploy: ## deploy your code to AWS
	@echo "+ $@"
	@chalice deploy

local: ## run local instance of the lambda
	@echo "+ $@"
	@chalice local

install: ## initiate the local environment
	@echo "+ $@"
	@pip -q install -r ./requirements_dev.txt
{%- if cookiecutter.use_pre_commit == 'y' %}
	@pre-commit install;
{%- endif %}
