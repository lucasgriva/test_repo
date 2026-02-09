# Variables - change these to fit your project
APP_NAME = my-awesome-app
VERSION = 1.0.0
PORT = 3000

# The default 'target' when you just type 'make'
.DEFAULT_GOAL := help

.PHONY: build run stop clean help

## build: Build the Docker image
build:
	docker build -t $(APP_NAME):$(VERSION) .

## run: Run the container in detached mode
run:
	docker run -d -p $(PORT):$(PORT) --name $(APP_NAME) $(APP_NAME):$(VERSION)

## stop: Stop and remove the container
stop:
	docker stop $(APP_NAME) || true
	docker rm $(APP_NAME) || true

## clean: Remove the Docker image
clean: stop
	docker rmi $(APP_NAME):$(VERSION)

## help: Show this help message
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^##' $(MAKEFILE_LIST) | sed -e 's/^## //'
