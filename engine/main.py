from app.core.db import init_db
from app.exceptions.handler import CustomHandler
from resources.v1 import api_v1

from fastapi import FastAPI


from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    origins = [
        "*"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    init_db()
    
    CustomHandler.register(app)
    
    app.include_router(api_v1)

    @app.get("/")
    def home() -> dict:
        return {"message": "application works!"}

    return app


app = create_app()
