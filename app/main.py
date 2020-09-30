from fastapi import FastAPI
from app.core.router import core_router

app = FastAPI()
app.include_router(core_router)

