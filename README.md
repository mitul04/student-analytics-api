# Student Analytics API

A FastAPI project for managing student records and exploring academic analytics, backed by PostgreSQL. This README also tracks the project's current learning phases and development roadmap.

## Tech stack

- **FastAPI** for the REST API
- **Swagger UI and OpenAPI** for interactive API documentation (`/docs`)
- **SQLAlchemy ORM** for database access and ORM model mapping
- **Pydantic** for request data validation
- **PostgreSQL** for relational data storage
- **Psycopg 2** (`psycopg2-binary`) for the PostgreSQL driver
- **Pytest** for running tests
- **FastAPI TestClient** for API tests
- **Uvicorn** as the ASGI development server

Run venv -------------------------------------------------------------------------------------------------------
venv/scripts/activate
uvicorn main:app --reload

View used libraries --------------------------------------------------------------------------------------------
python -m pip freeze > requirements.txt

Analyze route testing and codebase coverage --------------------------------------------------------------------
pytest -v
pytest --cov=routes --cov-report=term-missing

Learning phases ------------------------------------------------------------------------------------------------
REST API             ██████████ 100%
Backend Design       ██████████  95%
Analytics            █████████░  90%
Database             ██████░░░░  60%
Validation           ████████░░  80%
Testing              ██████░░░░  60%
Authentication       ░░░░░░░░░░   0%
Deployment           ░░░░░░░░░░   0%
Data Analysis        ░░░░░░░░░░   0%
Machine Learning     ░░░░░░░░░░   0%

Project evolution ----------------------------------------------------------------------------------------------
CRUD -> Analytics -> Database -> Richer dataset -> ML

Our immediate roadmap

We're going to make the transition  in small, understandable steps:

1. Finish the SQL foundation       ← almost there
          ↓
2. Connect Python to PostgreSQL
          ↓
3. Learn what a DB connection actually does
          ↓
4. Use raw SQL from Python
          ↓
5. Notice the problems with raw SQL
          ↓
6. Introduce SQLAlchemy
          ↓
7. Create SQLAlchemy models
          ↓
8. Replace the `students` list
          ↓
9. Adapt the FastAPI CRUD routes
          ↓
10. Move analytics onto database queries

The important part is step 4 → 5 → 6.
