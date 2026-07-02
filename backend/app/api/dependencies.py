from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.user_service import UserService


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_user_service() -> UserService:
    """
    Return a UserService instance.
    """

    return UserService()