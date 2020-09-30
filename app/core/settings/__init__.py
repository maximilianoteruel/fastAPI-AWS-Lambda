import os
from functools import lru_cache
from .base import BaseSettings
from .dev import DevSettings
from .prod import ProdSettings


@lru_cache()
def get_settings():
    environment = os.getenv("ENVIRONMENT", "DEV")

    if environment == "DEV":
        return DevSettings()
    elif environment == "PROD":
        return ProdSettings()
    else:
        return BaseSettings()
