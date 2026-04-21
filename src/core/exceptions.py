from fastapi import Request, status
from fastapi.responses import JSONResponse


class EnterpriseAPIException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code


async def enterprise_exception_handler(request: Request, exc: EnterpriseAPIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": {"message": exc.message, "type": exc.__class__.__name__},
        },
    )
