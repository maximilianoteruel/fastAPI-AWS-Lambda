from sqlalchemy.orm import Session

from app.cruds.notes import create_note, get_note, get_notes
from app.models.notes import Note
from app.schemas.notes import NoteCreate
from app.tests.utils.utils import random_string


def test_create_note(db: Session) -> None:

    db.query(Note).delete()

    title = random_string(100)
    description = random_string(255)
    tags = random_string(100)

    note_in = NoteCreate(title=title, description=description, tags=tags)
    note = create_note(db=db, note=note_in)

    assert note.title == title
    assert note.description == description
    assert note.tags == tags


def test_get_note(db: Session) -> None:

    db.query(Note).delete()

    title = random_string(100)
    description = random_string(255)
    tags = random_string(100)

    note_in = NoteCreate(title=title, description=description, tags=tags)
    note = create_note(db=db, note=note_in)

    stored_note = get_note(db=db, id=note.id)
    assert stored_note
    assert note.id == stored_note.id
    assert note.title == stored_note.title
    assert note.description == stored_note.description
    assert note.tags == stored_note.tags


def test_get_notes(db: Session) -> None:

    db.query(Note).delete()

    stored_notes = get_notes(db=db)
    assert len(stored_notes) == 0

    for _ in range(10):
        title = random_string(100)
        description = random_string(255)
        tags = random_string(100)

        note_in = NoteCreate(title=title, description=description, tags=tags)
        create_note(db=db, note=note_in)

    stored_notes = get_notes(db=db)
    assert len(stored_notes) == 10

    for _ in range(10):
        title = random_string(100)
        description = random_string(255)
        tags = random_string(100)

        note_in = NoteCreate(title=title, description=description, tags=tags)
        create_note(db=db, note=note_in)

    stored_notes = get_notes(db=db)
    assert len(stored_notes) == 20
