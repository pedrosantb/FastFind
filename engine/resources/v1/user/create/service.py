from app.exceptions.custom_exceptions import CustomException
from utils.decorators.create_session import create_session
from models.entities.user import User

from sqlmodel import Session, select

from .schema import CreateUserSchema

class CreateUserService:
    @staticmethod
    @create_session
    def create(session: Session, args: CreateUserSchema) -> dict:

        query = select(User).where(User.email == args.email)
        user = session.exec(query).one_or_none()

        if user:
            raise CustomException.email_already_in_use()

        new_user = User(email=args.email, username=args.username, image=args.image)
        session.add(new_user)
        session.flush()
        
        session.commit()

        return new_user.model_dump()    