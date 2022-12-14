export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

#all: down build up test
all: down build up

build:
	docker-compose build

up:
	docker-compose up -d certbot

down:
	docker-compose down --remove-orphans

test: up
	docker-compose run --rm --no-deps --entrypoint=pytest certbot /tests/unit /tests/integration /tests/e2e

unit-tests:
	docker-compose run --rm --no-deps --entrypoint=pytest certbot /tests/unit

integration-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest certbot /tests/integration

e2e-tests: up
	docker-compose run --rm --no-deps --entrypoint=pytest certbot /tests/e2e

logs:
	docker-compose logs certbot | tail -100

black:
	black -l 86 $$(find * -name '*.py')