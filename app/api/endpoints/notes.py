from typing import Any, List
from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from api import deps


from cruds import notes as cruds
from schemas import notes as schemas

router = APIRouter()


@router.get("/", response_model=List[schemas.Note])
async def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)) -> Any:
    notes = cruds.get_notes(db, skip=skip, limit=limit)
    return notes
