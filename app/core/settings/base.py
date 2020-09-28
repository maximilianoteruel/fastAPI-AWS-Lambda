import os
from pydantic import BaseSettings


class Settings(BaseSettings):

    SECRET_KEY: str = "fj49fj39fnsjh29dgasKkjHhgygoihUqjc921hc82bfhks92d6773"

    DATABASE_HOST: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_NAME: str

