from fastapi import HTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)


class EmailAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_400_BAD_REQUEST,
            detail="Email already exists.",
        )


class WeakPasswordException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_400_BAD_REQUEST,
            detail=(
                "Password must contain at least 8 characters, "
                "one uppercase letter, one lowercase letter, "
                "and one number."
            ),
        )


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail="User not found.",
        )