
from pydantic import BaseModel
from typing import Literal, List, Optional, Dict, Any



class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = 1.0
    max_tokens: Optional[int] = None
    top_p: Optional[float] = 1.0
    
    timeout_ms: Optional[int] = 60000  # Timeout for the request in milliseconds
    
    

class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class TraceInfo(BaseModel):
    request_id: str
    provider: str
    model: str
    latency_ms: int
    details: Optional[Dict[str, Any]] = None


class ChatResponse(BaseModel):
    id: str

    created: int
    model: str
    output_text: str
    finish_reason: str

    usage: Usage
    trace: TraceInfo

    cost: Optional[dict] = None