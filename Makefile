.PHONY: sync makemigrations migrate createsuperuser runserver test shell check

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
