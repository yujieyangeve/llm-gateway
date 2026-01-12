from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class GatewayError(Exception):
    """Base class for all gateway errors."""
    code: str = "gateway_error"
    status_code: int = 500
    message: str = "An unknown gateway error occurred."
    details: Optional[Dict[str, Any]] = None


    def __str__(self):
        return f"{self.code}: {self.status_code} - {self.message}"
    

class InvalidRequestError(GatewayError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__("INVALID_REQUEST", 400, message, details)


class UnauthorizedError(GatewayError):
    def __init__(self, message: str = "Unauthorized", details=None):
        super().__init__("UNAUTHORIZED", 401, message, details)


class ProviderTimeoutError(GatewayError):
    def __init__(self, message: str = "Provider timeout", details=None):
        super().__init__("PROVIDER_TIMEOUT", 504, message, details)


class ProviderUnavailableError(GatewayError):
    def __init__(self, message: str = "Provider unavailable", details=None):
        super().__init__("PROVIDER_UNAVAILABLE", 503, message, details)


class RateLimitedError(GatewayError):
    def __init__(self, message: str = "Rate limited", details=None):
        super().__init__("RATE_LIMITED", 429, message, details)