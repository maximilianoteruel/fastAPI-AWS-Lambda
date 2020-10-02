from .base import Settings


class DevSettings(Settings):
    API_HOST = "http://192.168.0.30:8000"
    SECRET_KEY = "fj49fj39fnsjh29dgasKkjHhgygoihUqjc921hc82bfhks92d6773"

    JWT_ALGORITHM = "HS256"
    JWT_EXPIRE_MINUTES = 30
