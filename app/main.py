import os
from fastapi import FastAPI
from core.settings import DevSettings, ProdSettings
from api.router import api_router

# Settings
environment = os.getenv("ENVIRONMENT", "DEV")

if environment == "DEV":
    settings = DevSettings()
elif environment == "PROD":
    settings = ProdSettings()


# FastAPI
app = FastAPI()
app.include_router(api_router)
