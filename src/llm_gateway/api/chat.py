
from llm_gateway.domain.models import ChatRequest
from llm_gateway.providers.mock_provider import MockedProvider
from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter(prefix="/v1")

provider = MockedProvider()

@router.post("/chat")
async def chat_endpoint(request: Request, body: ChatRequest):

    response = provider.generate_response(body)
    response.trace.request_id = request.state.request_id

    return response
