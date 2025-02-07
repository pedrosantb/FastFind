from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse

from utils.api.response import create_response

from .create.schema import CreateUserSchema
from .create.service import CreateUserService

from .read.service import ReadUserService

user_router = APIRouter(prefix='/user')

@user_router.get('/{user_email}')
def get_user(user_email: str ,request: Request):
    user = ReadUserService.read(user_email)
    return user


@user_router.post('/')
def create_user(params: CreateUserSchema, request: Request):
    user = CreateUserService.create(args=params)
    return create_response(data=user)