from app.exceptions.custom_exceptions import CustomException
from utils.decorators.create_session import create_session
from models.entities.user import User

from sqlmodel import Session, select
from sqlmodel.sql.expression import Select

from pydantic import EmailStr

class ReadUserService:
    @staticmethod
    @create_session
    def read(user_email: EmailStr, session: Session) -> dict:
        query = select(User).where(User.email == user_email)
        user = session.exec(query).first()
        if not user:
            raise CustomException.user_not_found()

        return user.model_dump()

