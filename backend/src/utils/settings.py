from pydantic import Field
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    user_name: str = Field(..., env="USER_NAME")
    db_name: str = Field(..., env="DB_NAME")
    password: str = Field(..., env="PASSWORD")

    class Config:
        env_file = ".env"


settings = Settings()


