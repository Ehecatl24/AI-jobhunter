from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db, get_user_service
from app.schemas.user import UserCreate, UserRead
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_create: UserCreate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service),
):
    """
    Register a new user.
    """

    user = user_service.create(
        db=db,
        user_create=user_create,
    )

    db.commit()

    db.refresh(user)

    return user