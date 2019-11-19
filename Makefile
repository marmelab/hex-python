.PHONY: default start test

.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

start: ## Start project
	@echo "Start the project"
	python3 src/main.py -f assets/board.json


test: ## Start project
	@echo "Launch tests"
	python3 -m unittest /home/ubuntu/PycharmProjects/hex-python/src/main_test.py

