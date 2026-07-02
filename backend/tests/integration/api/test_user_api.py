from sqlalchemy import select

from app.models.user import User


def test_create_user(client, db):
    """
    Create a user through the API.
    """

    response = client.post(
        "/api/v1/users",
        json={
            "email": "integration@test.com",
            "password": "Password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == "integration@test.com"

    user = db.scalar(
        select(User).where(
            User.email == "integration@test.com"
        )
    )

    assert user is not None

    assert user.password_hash != "Password123"