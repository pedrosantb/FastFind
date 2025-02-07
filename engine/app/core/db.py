from app.core import config
from sqlmodel import create_engine

engine = create_engine(str(config.SQLALCHEMY_DATABASE_URI))


def init_db() -> None:
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)
