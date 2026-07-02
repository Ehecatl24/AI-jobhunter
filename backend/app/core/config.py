from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Global application settings.

    Every configuration value should be accessed
    through this class.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore"
    )

    # ==========================
    # Project
    # ==========================

    PROJECT_NAME: str
    PROJECT_VERSION: str
    ENVIRONMENT: str
    DEBUG: bool

    # ==========================
    # API
    # ==========================

    API_V1_PREFIX: str

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # ==========================
    # Database
    # ==========================

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    # ==========================
    # Redis
    # ==========================

    REDIS_HOST: str
    REDIS_PORT: int

    # ==========================
    # OpenAI
    # ==========================

    OPENAI_API_KEY: str = ""

    # ==========================
    # Logging
    # ==========================

    LOG_LEVEL: str

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+psycopg2://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings instance.
    """
    return Settings()


settings = get_settings()