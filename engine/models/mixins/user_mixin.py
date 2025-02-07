from typing import Optional, Self

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserMixin(SQLModel):
    email: EmailStr = Field(unique=True)
  