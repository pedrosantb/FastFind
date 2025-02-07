from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class BaseMixin(SQLModel):
    id: int = Field(unique=True, nullable=False, primary_key=True)
    created_at: datetime = datetime.now(timezone.utc)
    updated_at: Optional[datetime] = datetime.now(
        timezone.utc
    )  # TODO: refatorar definição de valor padrão.
    deleted_at: Optional[datetime] = Field(default=None, nullable=True)
    is_active: bool = Field(default=True)
    created_by: Optional[int] = Field(nullable=True)
    updated_by: Optional[int] = Field(nullable=True)
