from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_password: str
    database_port: str
    database_name: str
    database_username: str

    class config:
        env_file= ".env"
