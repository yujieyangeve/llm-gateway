from abc import ABC, abstractmethod
from llm_gateway.domain.chat_models import ChatRequest, ChatResponse

class ChatProvider(ABC):

    @abstractmethod
    async def chat(self, request: ChatRequest) -> ChatResponse:
        pass
