from llm_gateway.domain.error import GatewayError 
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

async def gate_way_exception_handler(request: Request, exc : GatewayError):
    return JSONResponse(
        status_code=400,
        content={"error": {"code": exc.code, "message": exc.message, "details": exc.details}, 
                 "trace": {"request_id": request.state.request_id}},
    )


async def unknown_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "internal_server_error",
                "message": "An internal server error occurred.",
                "details": str(exc),
            },
            "trace": {"request_id": request.state.request_id},
        },
    )