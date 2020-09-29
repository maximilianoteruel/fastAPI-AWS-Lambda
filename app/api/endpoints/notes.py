from fastapi import APIRouter, Depends, HTTPException

# from core.database import get_db

# from cruds import notes

router = APIRouter()


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @router.get("/")
# async def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     notes = get_notes(db, skip=skip, limit=limit)
#     return notes
