from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}
