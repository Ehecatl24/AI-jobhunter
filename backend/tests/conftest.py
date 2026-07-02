from collections.abc import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.config import settings
from app.db.base import Base


TEST_DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"jobhunter_test"
)

engine = create_engine(
    TEST_DATABASE_URL,
    future=True,
)

TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


@pytest.fixture(scope="session", autouse=True)
def create_database() -> Generator[None, None, None]:
    """
    Create all database tables before tests and
    remove them afterwards.
    """

    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def db() -> Generator[Session, None, None]:
    """
    Return an isolated database session.
    """

    session = TestingSessionLocal()

    try:
        yield session

        session.rollback()

    finally:
        session.close()