.PHONY: default start test

CONTAINER_NAME = python_hex
PWD = $(shell pwd)
DOCKER := docker run -it --rm $(CONTAINER_NAME)

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

start: ## Start project
	@echo "Start the project"
	$(DOCKER) python3 src/main.py -f assets/board.json

install: ## Build the docker
	@echo "Build the container"
	docker build -t $(CONTAINER_NAME) .

test: ## Test the project
	@echo "Launch tests"
	$(DOCKER) pytest -v --pyargs src
