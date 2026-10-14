from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import sessionmaker
from my_credentials import *


#DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
#engine = create_engine(DATABASE_URL, echo=True)

def create_database_engine(database_name: str):
    url = URL.create(
        "postgresql+psycopg2",
        username=USERNAME,
        password=PASSWORD,
        host=HOST,
        port=int(PORT),
        database=database_name,
    )
    return create_engine(url, echo=True)

engine = create_database_engine(DATABASE)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

test_engine = create_database_engine("student_analytics_test")

TestSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False
)

#with engine.connect() as connection:
#    result = connection.execute(text("SELECT 1"))
#    print(result.scalar())

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()