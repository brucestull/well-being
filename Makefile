.DEFAULT_GOAL := help
.PHONY: help sync makemigrations migrate createsuperuser runserver test shell check

help:
	@echo "Available targets:"
	@echo "  sync            - Install/update dependencies from lockfile"
	@echo "  makemigrations  - Create new Django migrations"
	@echo "  migrate         - Apply Django migrations"
	@echo "  createsuperuser - Create a Django admin user"
	@echo "  runserver       - Run the Django development server"
	@echo "  test            - Run Django tests"
	@echo "  shell           - Open a Django shell"
	@echo "  check           - Run Django system checks"

sync:
	uv sync

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

createsuperuser:
	uv run python manage.py createsuperuser

runserver:
	uv run python manage.py runserver

test:
	uv run python manage.py test

shell:
	uv run python manage.py shell

check:
	uv run python manage.py check
