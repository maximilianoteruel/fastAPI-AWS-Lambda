from sqlalchemy.orm import Session

from app.cruds.notes import create_note, get_note, get_notes
from app.schemas.notes import NoteCreate


def test_create_note(db: Session) -> None:
    title = "title test example"
    description = "description test example"
    tags = "tags test example"
    note_in = NoteCreate(title=title, description=description, tags=tags)
    note = create_note(db=db, note=note_in)
    assert note.title == title
    assert note.description == description
    assert note.tags == tags


def test_get_note(db: Session) -> None:
    title = "title test example"
    description = "description test example"
    tags = "tags test example"
    note_in = NoteCreate(title=title, description=description, tags=tags)
    note = create_note(db=db, note=note_in)

    stored_note = get_note(db=db, id=note.id)
    assert stored_note
    assert note.id == stored_note.id
    assert note.title == stored_note.title
    assert note.description == stored_note.description
    assert note.tags == stored_note.tags
