from app.exceptions.custom_exceptions import ApiException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from models.enums.http_status import HttpStatusEnum
from utils.api.response import create_response


class CustomHandler:
    @staticmethod
    def register(app: FastAPI) -> None:

        @app.exception_handler(Exception)
        def general_exception(request: Request, exception: Exception) -> JSONResponse:
            return create_response(
                http_status=HttpStatusEnum.INTERNAL_SERVER_ERROR,
                error_message='Internal Server Error',
            )

        @app.exception_handler(ApiException)
        def http_exception_handler(
            request: Request, exception: ApiException
        ) -> JSONResponse:
            return create_response(
                http_status=exception.http_status, error_message=exception.message
            )
