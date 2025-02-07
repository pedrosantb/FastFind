import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

load_dotenv()

driver = os.environ["DB_DRIVER"]
user = os.environ["DB_USER"]
password = os.environ["DB_PASSWORD"]
host = os.environ["DB_HOST"]
port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]

SQLALCHEMY_DATABASE_URI = (
    os.getenv('DATABASE_URL') or f"{driver}://{user}:{password}@{host}:{port}/{db_name}"
)

engine = create_engine(url=SQLALCHEMY_DATABASE_URI)
