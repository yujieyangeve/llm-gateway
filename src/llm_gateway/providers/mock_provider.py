
import time
import uuid
from src.llm_gateway.domain.models import ChatRequest, ChatResponse, TraceInfo, Usage


class MockedProvider:
    """A mocked LLM provider for testing purposes."""

    def generate_response(self, request: ChatRequest) -> ChatResponse:
        startTime = time.perf_counter()

        
        return ChatResponse(
            id=str(uuid.uuid4()),
            created=int(time.time()),

            model=request.model,
            output_text=f"Mocked response to: {request.messages[-1].content}",
            finish_reason="stop",
            usage=Usage(prompt_tokens=10, completion_tokens=20, total_tokens=30),
           
            trace=TraceInfo(
                request_id="mocked-request-id",
                provider="mocked_provider",
                model=request.model,
                latency_ms=int((time.perf_counter() - startTime) * 1000),
                details=None
            ),
            cost=None
        )
    
