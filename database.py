import os
from dotenv import load_dotenv

from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import sessionmaker


load_dotenv()

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")
DATABASE = os.getenv("DB_NAME", "student_analytics")
TEST_DATABASE = os.getenv("TEST_DB_NAME", "student_analytics_test")

if not USERNAME or PASSWORD is None:
    raise RuntimeError(
        "DB_USERNAME and DB_PASSWORD must be configured."
    )


def create_database_engine(database_name: str):
    url = URL.create(
        "postgresql+psycopg2",
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=int(PORT),
        database=database_name,
    )
    return create_engine(url)

engine = create_database_engine(DATABASE)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()