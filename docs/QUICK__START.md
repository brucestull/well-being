# QUICK START (DEV)

## Prerequisites
- Python 3.12+
- `uv` installed (`pip install uv`)

## Setup
From repository root:

```bash
uv sync
```

## Run migrations

```bash
uv run python manage.py migrate
```

## Create an admin user (optional)

```bash
uv run python manage.py createsuperuser
```

## Run the development server

```bash
uv run python manage.py runserver
```

## Run tests

```bash
uv run python manage.py test
```
