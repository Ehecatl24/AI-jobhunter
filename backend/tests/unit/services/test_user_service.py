from app.schemas.user import UserCreate
from app.services.user_service import UserService


def test_create_user(db):
    """
    A user can be created successfully.
    """

    service = UserService()

    user = service.create(
        db=db,
        user_create=UserCreate(
            email="john@example.com",
            password="Password123",
        ),
    )

    db.commit()

    assert user.id is not None
    assert user.email == "john@example.com"

    # Password must never be stored in plain text
    assert user.password_hash != "Password123"

    # Password hash should not be empty
    assert len(user.password_hash) > 20
