from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.correlation import generate_correlation_id
from app.utils.logger import logger

class RequestMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        correlation_id = generate_correlation_id()
        logger.info(
            f"Incoming request | "
            f"CorrelationID={correlation_id} | "
            f"Path={request.url.path}"
        )

        response = await call_next(request)

        response.headers["X-Correlation-ID"] = correlation_id

        return response