from models.mixins.base_mixin import BaseMixin
from models.mixins.user_mixin import UserMixin
from pydantic import EmailStr

from sqlmodel import Field, Relationship

class User(BaseMixin, UserMixin, table=True):
    email: EmailStr = Field(unique=True, index=True, max_length=255)
    username: str = Field(max_length=255, nullable=True)
    image: str = Field(nullable=True)

    reviews: list["Reviews"] = Relationship(cascade_delete=True)
  


    def __repr__(self) -> str:
        return (
            f'User('
            f'id={self.id}, '
            f'email={self.email!r}, '
            f'username={self.username!r}, '
            f'image={self.image!r}'
            f')' 
        )

    def __str__(self) -> str:
        return f'<User {self.username}>'