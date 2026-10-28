from database import create_database_engine, TEST_DATABASE
from sqlalchemy.orm import sessionmaker

test_engine = create_database_engine(TEST_DATABASE)

TestSessionLocal = sessionmaker(
    bind=test_engine,
    autoflush=False,
    autocommit=False,
)