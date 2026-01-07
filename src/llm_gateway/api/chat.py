from llm_gateway.domain.models import ChatRequest
from llm_gateway.providers.openai_provider import OpenAIProvider
from fastapi import APIRouter
from starlette.requests import Request


router = APIRouter(prefix="/v1")


@router.post("/chat")
async def chat_endpoint(request: Request, body: ChatRequest):

    provider = OpenAIProvider(
        client=request.app.state.openai_client,
        model_mapping={"gpt-4o-mini": "gpt-4o-mini"},
    )

    response = await provider.chat(body)
    response.trace.request_id = request.state.request_id

    return response
