from fastapi import Response
from fastapi.responses import JSONResponse

from models.enums.http_status import HttpStatusEnum



def create_response(
    data: dict = {},
    http_status: HttpStatusEnum = HttpStatusEnum.OK,
    error_message: str = '',
    **kwargs: dict
) -> JSONResponse:


    content = {
        'data': {'result': data} if data else {},
    }
    error = {}

    if error_message:
        error = {
            "code": http_status.name.title().replace('_', ' '),
            "message": error_message,
        }

        content['error'] = error

    response = JSONResponse(content=content, status_code=http_status.value)

    return response

