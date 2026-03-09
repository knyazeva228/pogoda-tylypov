from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # База данных MySQL
    mysql_user: str = "root"
    mysql_password: str = "rootpassword"
    mysql_db: str = "weather"
    mysql_host: str = "db"
    mysql_port: int = 3306

    @property
    def database_url(self) -> str:
        # Используем диалект mysql+asyncmy
        return f"mysql+asyncmy://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}:{self.mysql_port}/{self.mysql_db}"

    # Redis
    redis_host: str = "redis"
    redis_port: int = 6379
    redis_db: int = 0

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    celery_broker_url: str = Field(alias="CELERY_BROKER_URL", default=None)
    celery_result_backend: str = Field(alias="CELERY_RESULT_BACKEND", default=None)

    webhook_secret: str = "my-super-secret-key-change-in-production"
    rate_limit_per_minute: int = 60

    class Config:
        env_file = ".env"

settings = Settings()