from os import getenv


class Settings:
    def __init__(self):
        self.server = ServerSettings()
        self.logging = LoggingSettings()
        self.provider = ProvideSettings()

        self.provider.validate_provider()


class LoggingSettings:
    def __init__(self):
        self.log_file = getenv("LOG_FILE", "app.log")
        self.log_level = getenv("LOG_LEVEL", "INFO")
        self.log_format = getenv("LOG_FORMAT", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

class ServerSettings:
    def __init__(self):
      
        self.timeout = int(getenv("TIMEOUT", "30")) # in seconds    
        self.debug_mode = getenv("DEBUG_MODE", "false").lower() == "true"
        self.max_retries = int(getenv("MAX_RETRIES", "3"))
        self.log_level = getenv("LOG_LEVEL", "INFO")


class openAISettings:
    def __init__(self):
        self.api_key = getenv("API_KEY", "default_key")
        self.base_url = getenv("OPENAI_API_URL", "https://api.openai.com/v1")
        self.max_retries = int(getenv("OPENAI_MAX_RETRIES", "3"))
        self.enabled = getenv("OPENAI_ENABLED", "true").lower() == "true"
        self.model_name = getenv("OPENAI_MODEL_NAME", "gpt-4")
        self.temperature = float(getenv("OPENAI_TEMPERATURE", "0.7"))
        self.max_tokens = int(getenv("OPENAI_MAX_TOKENS", "2048"))
        self.top_p = float(getenv("OPENAI_TOP_P", "1.0"))
      
  
class ProvideSettings:
    def __init__(self):
        self.default_provider = getenv("DEFAULT_PROVIDER", "openai")
        self.openai = openAISettings()

    def validate_provider(self):
        enabled = []
        if self.openai.enabled:
            enabled.append("openai")
        if not enabled:
            raise ValueError("No LLM providers are enabled.")   
        
        if self.openai.enabled and not self.openai.api_key:
            raise ValueError("OpenAI API key is not set.")
