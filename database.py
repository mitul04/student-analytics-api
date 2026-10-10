from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from my_credentials import *


DATABASE_URL = f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
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