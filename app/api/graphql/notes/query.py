# GraphQL
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

# Core
from app.core.db.session import SessionScoped

# Types
from .types import NoteType, NoteTypeRelay

# Cruds
from app.cruds.notes import crud_note

# Note by ID
class QueryNote:
    note = graphene.Field(NoteType, id=graphene.Argument(graphene.ID, required=True))

    def resolve_note(self, info, id):
        return crud_note.get(db=SessionScoped, id=id)


# List of Notes
class QueryNotesList:
    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return crud_note.get_multi(db=SessionScoped)


# Relay of Notes
class QueryNotesRelay:
    notes_relay = SQLAlchemyConnectionField(NoteTypeRelay.connection)
