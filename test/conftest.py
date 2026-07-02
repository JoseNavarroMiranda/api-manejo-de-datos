import os

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = "clave-secreta-pruebas"
os.environ["ALGORITHM"] = "HS256"
os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "15"

import sqlite3
from datetime import datetime, timezone

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

from app.database import Base
from app.models import User

from app.models.users import User
from app.utils.security import hash_password



engine = create_engine("sqlite:///:memory:", 
                       connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def _sqlite_sysdatetimeoffset():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")

@event.listens_for(engine, "connect")
def _register_sqlite_functions(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        dbapi_connection.create_function("sysdatetimeoffset", 0, _sqlite_sysdatetimeoffset)


@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session():
    session = TestingSessionLocal()
    yield session
    session.close()


@pytest.fixture
def users_test(db_session):
    user = User(username="testusuario", password=hash_password("Holamundo2026*"), role="editor", status=True)
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user

@pytest.fixture
def users_test1(db_session):
    user = User(username="testusuarioadmin", password=hash_password("Holamundo2026*", role="admin", status=True))
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def users_test2(db_session):
    user = User(username="testuviewer", password=hash_password("Holamundo2026*", role="viewer", status=True))
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user