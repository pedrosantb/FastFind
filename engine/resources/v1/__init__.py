from fastapi import APIRouter

from .user.controller import user_router

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)