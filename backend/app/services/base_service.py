from datetime import UTC, datetime
from typing import Generic, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.base import Base

T = TypeVar("T", bound=Base)


class BaseService(Generic[T]):
    """
    Generic CRUD service.

    This class implements common CRUD operations shared by
    every domain service.
    """

    def __init__(self, model: type[T]):
        self.model = model

    def get_by_id(
        self,
        db: Session,
        entity_id: UUID,
    ) -> T | None:
        """
        Return an entity by its UUID.
        """

        stmt = (
            select(self.model)
            .where(self.model.id == entity_id)
            .where(self.model.deleted_at.is_(None))
        )

        return db.scalar(stmt)

    def list(
        self,
        db: Session,
    ) -> list[T]:
        """
        Return every active entity.
        """

        stmt = (
            select(self.model)
            .where(self.model.deleted_at.is_(None))
            .order_by(self.model.created_at)
        )

        return list(db.scalars(stmt).all())

    def create(
        self,
        db: Session,
        entity: T,
    ) -> T:
        """
        Add a new entity.

        This method DOES NOT commit the transaction.
        """

        db.add(entity)

        db.flush()

        db.refresh(entity)

        return entity

    def update(
        self,
        db: Session,
        entity: T,
    ) -> T:
        """
        Flush pending changes.

        This method DOES NOT commit.
        """

        db.flush()

        db.refresh(entity)

        return entity

    def soft_delete(
        self,
        db: Session,
        entity: T,
    ) -> T:
        """
        Soft delete an entity.

        This method DOES NOT commit.
        """

        entity.deleted_at = datetime.now(UTC)

        db.flush()

        return entity