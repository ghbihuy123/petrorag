from pydantic_settings import BaseSettings, SettingsConfigDict

class CommonSettings(BaseSettings):
    chat_endpoint: str = "http://chat_svc:8081"

    model_config = SettingsConfigDict(
        case_sensitive=False
    )

common_settings = CommonSettings()