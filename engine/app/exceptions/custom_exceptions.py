from models.enums.http_status import HttpStatusEnum


class ApiException(Exception):
    def __init__(
        self,
        message: str = None,
        http_status: HttpStatusEnum = HttpStatusEnum.BAD_REQUEST,
        *args,
        **kwargs
    ) -> None:
        self.message = message
        self.http_status = http_status
        super().__init__(*args, **kwargs)


class CustomException:

    @staticmethod
    def user_not_found() -> ApiException:
        api_exception = ApiException(
            message='Wrong Email or Password',
            http_status=HttpStatusEnum.BAD_REQUEST,
        )

        return api_exception

    @staticmethod
    def forbidden() -> ApiException:
        api_exception = ApiException(
            message='NNot allowed', http_status=HttpStatusEnum.FORBIDDEN
        )

        return api_exception

    @staticmethod
    def user_not_authenticated() -> ApiException:
        api_exception = ApiException(
            message='User not authenticated', http_status=HttpStatusEnum.UNAUTHORIZED
        )

        return api_exception

    @staticmethod
    def internal_server_error() -> ApiException:
        api_exception = ApiException(
            message='Internal server error', http_status=HttpStatusEnum.INTERNAL_SERVER_ERROR
        )
        
        return api_exception
    
    
    @staticmethod
    def service_unavailable() -> ApiException:
        api_exception = ApiException(
            message='The service is not available at the moment. Try again later',
            http_status=HttpStatus.SERVICE_UNAVAILABLE
        )
        return api_exception
