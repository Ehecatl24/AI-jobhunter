from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    """
    Common user fields.
    """

    email: EmailStr


class UserCreate(UserBase):
    """
    Payload used to create a user.
    """

    password: str = Field(
        min_length=8,
        max_length=128,
        description="User password",
    )


class UserRead(UserBase):
    """
    User returned by the API.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    is_active: bool

    is_verified: bool

    created_at: datetime

    updated_at: datetime


class UserUpdate(BaseModel):
    """
    Fields that can be updated.
    """

    email: EmailStr | None = None

    model_config = ConfigDict(from_attributes=True)