import time
from typing import Any
import uuid
from llm_gateway.domain.models import ChatRequest, ChatResponse, TraceInfo, Usage
from llm_gateway.providers.base import ChatProvider
from llm_gateway.domain.error import (
    UnauthorizedError,
    InvalidRequestError,
    RateLimitedError,
)


class OpenAIProvider(ChatProvider):
    """An OpenAI LLM provider implementation."""
    def __init__(self, client, model_mapping: dict):
        self.client = client
        self.model_mapping = model_mapping
        self.provider_name = "openai"

    async def chat(self, request: ChatRequest) -> ChatResponse:
        startTime = time.perf_counter()

        messages = [{"role": msg.role, "content": msg.content} for msg in request.messages]

        payload = {
            "model": self.resolve_model(request.model),
            "messages": messages,
            "temperature": request.temperature,
            "top_p": request.top_p,
        }
        print("Payload for OpenAI:", payload)
        if request.max_tokens:
            payload["max_tokens"] = request.max_tokens

        try:
            response = await self.client.chat.completions.create(**payload)
        except Exception as e:
            print("Error from OpenAI:", str(e))
            message = str(e).lower()
            if "rate limit" in message:
                raise RateLimitedError("Rate limit exceeded for OpenAI provider.")
            elif "unauthorized" in message:
                raise UnauthorizedError("Invalid API key provided.")
            else:
                raise InvalidRequestError(
                    "Invalid request to OpenAI provider.", e.message
                )
        choice = response.choices[0]

        return ChatResponse(
            id=str(uuid.uuid4()),
            created=int(time.time()),
            model=request.model,
            output_text=choice.message.content,
            finish_reason=choice.finish_reason,
            usage=Usage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            ),
            trace=TraceInfo(
                request_id="from middleware",
                provider=self.provider_name,
                model=request.model,
                latency_ms=int((time.perf_counter() - startTime) * 1000),
                details=None,
            ),
            cost=None,
        )

    def resolve_model(self, requested_model: str) -> str:
        return self.model_mapping.get(requested_model, requested_model)
