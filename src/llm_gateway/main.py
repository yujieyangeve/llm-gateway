from llm_gateway.config.settings import Settings
from fastapi import FastAPI
from .api.chat import router as chat_router
from .middleware.auth import ApiKeyAuthMiddleware
from .middleware.request_id import RequestIDMiddleware
from .routing.router import health_router
from contextlib import asynccontextmanager
from openai import AsyncOpenAI

@asynccontextmanager
async def _lifespan(app: FastAPI):
    # ===== startup =====
    settings = app.state.settings
    openai_settings = settings.provider.openai

    print(openai_settings.api_key)
    openai_client = AsyncOpenAI(
        api_key=openai_settings.api_key,
        base_url=openai_settings.base_url,
        timeout=openai_settings.timeout_seconds,
    )
    app.state.openai_client = openai_client
    # - http session
    # - metrics / tracing
    yield
    # ===== shutdown =====
    await openai_client.close()

def _register_routes(app: FastAPI):
    print("Registering routes...")
    app.include_router(health_router())
    app.include_router(chat_router)

def _register_middlewares(app: FastAPI, settings: Settings):
    print("Registering middlewares...")
    app.add_middleware(RequestIDMiddleware)
    # app.add_middleware(ApiKeyAuthMiddleware, settings=settings)


# def _register_exception_handlers(app: FastAPI):
#     print("Registering exception handlers...")
#     app.add_exception_handler(Exception, generic_exception_handler)


def create_app(settings: Settings):
    app = FastAPI(title="LLM Gateway", version="1.0.0", lifespan=_lifespan, debug=settings.server.debug_mode)

    app.state.settings = settings

    _register_middlewares(app, settings)
    _register_routes(app)
    # _register_exception_handlers(app)
    return app


settings = Settings()
app = create_app(settings)
