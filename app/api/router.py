from fastapi import APIRouter

from .rest import notes

api_router = APIRouter()
api_router.include_router(notes.router, prefix="/notes", tags=["notes"])
