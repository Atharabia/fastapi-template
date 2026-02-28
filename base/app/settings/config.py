from pydantic_settings import BaseSettings


class Config(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    APP_NAME: str = "app"
    APP_VERSION: str = "1.0.0"
    APP_DEBUG: bool = False

    DATABASE_URL: str = ""

    JWT_KEY: str = ""
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY: int = 30
