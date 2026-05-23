from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.middleware.request_middleware import RequestMiddleware
from app.routes.ai_routes import router
from app.exceptions.handlers import global_exception_handler

limiter = Limiter(key_func=get_remote_address)

app = FastAPI(title="GenAI Platform", version="1.0")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, global_exception_handler)
app.add_middleware(SlowAPIMiddleware)
app.add_middleware(RequestMiddleware)

app.include_router(router)