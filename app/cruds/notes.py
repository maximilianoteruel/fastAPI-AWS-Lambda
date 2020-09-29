from sqlalchemy.orm import Session

from app.models.notes import Note
from app.schemas.notes import NoteCreate


def get_note(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Note).offset(skip).limit(limit).all()


def create_note(db: Session, note: NoteCreate):
    db_note = Note(**note.dict)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
