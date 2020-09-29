from fastapi import FastAPI
from api.router import api_router

# FastAPI
app = FastAPI()
app.include_router(api_router)
