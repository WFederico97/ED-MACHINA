import os
import sys
# Add the backend directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db.database import get_db
from main import app

SQLALCHEMY_DATABASE_URL = os.getenv("URL_TEST", "postgresql://postgres:postgres@localhost:5432/leads_api")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

test_session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)


Base = declarative_base()    

@pytest.fixture(scope="module")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = test_session_local(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="module")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            db_session.close()

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client