from pydantic_settings import BaseSettings
from pydantic import Field
import os
from dotenv import load_dotenv

# load_dotenv('./.env')
# print('--------------------------')
# print(os.environ.get("SECRET_KEY"))

class Settings(BaseSettings):
    database_hostname: str 
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int 

    class ConfigDict:
        env_file = '.env'


settings = Settings()