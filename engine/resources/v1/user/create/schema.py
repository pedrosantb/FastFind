from typing import Optional
from pydantic import BaseModel, EmailStr

class CreateUserSchema(BaseModel):

    email: Optional[EmailStr] = None
    username: Optional[str] = None
    image: Optional[str] = None