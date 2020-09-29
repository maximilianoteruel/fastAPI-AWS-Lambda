from .base import Settings


class DevSettings(Settings):
    API_HOST: str = "http://192.168.0.30:8000"

