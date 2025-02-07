from collections.abc import Callable
from functools import wraps

from app.core.config import engine
from sqlmodel import Session


def create_session(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Session(engine) as session:
            result = func(session=session, *args, **kwargs)

        return result

    return wrapper
