from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.exceptions import EmailAlreadyExistsException
from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.base_service import BaseService
from app.utils.password import validate_password


class UserService(BaseService[User]):
    """
    Business logic related to user management.

    Authentication is handled by AuthService.
    """

    def __init__(self) -> None:
        super().__init__(User)

    def get_by_email(
        self,
        db: Session,
        email: str,
    ) -> User | None:
        """
        Return a user by email.
        """

        stmt = (
            select(User)
            .where(User.email == email)
            .where(User.deleted_at.is_(None))
        )

        return db.scalar(stmt)

    def create(
        self,
        db: Session,
        user_create: UserCreate,
    ) -> User:
        """
        Create a new user.

        This method DOES NOT commit the transaction.
        """

        # Validate password policy (Fail Fast)
        validate_password(user_create.password)

        # Ensure email is unique
        if self.get_by_email(db, user_create.email):
            raise EmailAlreadyExistsException()

        # Create ORM entity
        user = User(
            email=user_create.email,
            password_hash=hash_password(
                user_create.password
            ),
        )

        # Persist entity without committing
        return super().create(
            db=db,
            entity=user,
        )