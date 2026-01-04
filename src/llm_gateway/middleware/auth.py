from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from llm_gateway.config.settings import Settings


class ApiKeyAuthMiddleware (BaseHTTPMiddleware):
    def __init__(self, app, settings: Settings):
        super().__init__(app)
        self.settings = settings

    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("X-API-KEY")
        if not api_key or api_key != self.settings.provider.api_key:
            return Response("Unauthorized", status_code=401)
        
        response: Response = await call_next(request)
        return response