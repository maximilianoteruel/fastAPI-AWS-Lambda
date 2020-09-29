from sqlalchemy.orm import Session

from app.cruds.base import CRUDBase

from app.models.notes import Note
from app.schemas.notes import NoteCreate, NoteUpdate


# def get_note(db: Session, id: int):
#     return db.query(Note).filter(Note.id == id).first()


# def get_notes(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(Note).offset(skip).limit(limit).all()


# def create_note(db: Session, note: NoteCreate):
#     db_note = Note(**note.dict())
#     db.add(db_note)
#     db.commit()
#     db.refresh(db_note)
#     return db_note


class CRUDNote(CRUDBase[Note, NoteCreate, NoteUpdate]):
    pass


crud_note = CRUDNote(Note)
