# Student Analytics API

A FastAPI project for managing student records and exploring academic analytics, backed by PostgreSQL. This README also tracks the project's current learning phases and development roadmap.

## Tech stack

- **FastAPI** for the REST API
- **Swagger UI and OpenAPI** for interactive API documentation (`/docs`)
- **Pydantic** for request data validation
- **PostgreSQL** for relational data storage
- **Psycopg 2** (`psycopg2-binary`) for the PostgreSQL driver
- **SQLAlchemy ORM** for database access and ORM model mapping
- **Pytest** for running tests
- **FastAPI TestClient** for API tests
- **Alembic** for database schema migrations and version control
- **Uvicorn** as the ASGI development server

## Create and activate the virtual environment 

python -m venv venv
venv/scripts/activate

## Run the development server

uvicorn main:app --reload

## Install dependencies in a fresh environment

pip install -r requirements.txt

## Export the installed libraries

pip freeze > requirements.txt

## Analyze route testing and codebase coverage

pytest -v
pytest --cov=routes --cov-report=term-missing

## Apply pending migrations and record migration in original table(s)

alembic upgrade head
alembic stamp head

## Generate a migration after modifying SQLAlvhemy models

alembic revision --autogenerate -m "describe schema change"  

## Check current migration revision

alembic current

## Learning phases

REST API             ██████████ 100%
Backend Design       ██████████  95%
Analytics            █████████░  90%
Database             █████████░  90%
Validation           █████████░  90%
Testing              ████████░░  80%
Authentication       ░░░░░░░░░░   0%
Deployment           ░░░░░░░░░░   0%
Data Analysis        ░░░░░░░░░░   0%
Machine Learning     ░░░░░░░░░░   0%

## Project evolution

CRUD → Analytics → Database → Richer Dataset → Machine Learning

## Original Learning Roadmap

We're making the transition in small, understandable steps:

1. Finish the SQL foundation
2. Connect Python to PostgreSQL
3. Learn what a database connection actually does
4. Use raw SQL from Python
5. Understand the problems with raw SQL
6. Introduce SQLAlchemy
7. Create SQLAlchemy models
8. Replace the in-memory students list
9. Adapt the FastAPI CRUD routes
10. Move analytics onto database queries

The important part is steps 4 → 5 → 6: understanding the limitations of raw SQL in application code before introducing an ORM.

## Current Development Direction

The project has progressed beyond the original SQLAlchemy learning phase. Current work focuses on:

- Database configuration through environment variables
- Separating development and test databases
- Managing schema changes with Alembic
- Defining API request and response schemas
- Testing database-backed CRUD and analytics endpoints
- Preparing the project for documentation and deployment