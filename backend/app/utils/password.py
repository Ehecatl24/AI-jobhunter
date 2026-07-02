import re

from app.core.exceptions import WeakPasswordException


def validate_password(password: str) -> None:
    """
    Validate password strength.

    Raises:
        WeakPasswordException: if the password does not
        satisfy the password policy.
    """

    pattern = (
        r"^(?=.*[a-z])"
        r"(?=.*[A-Z])"
        r"(?=.*\d)"
        r".{8,}$"
    )

    if not re.match(pattern, password):
        raise WeakPasswordException()