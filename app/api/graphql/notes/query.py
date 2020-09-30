# GraphQL
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# Types
from .types import NoteType, NoteTypeRelay


# Note by ID
class QueryNote:
    note = graphene.Field(NoteType, id=graphene.Argument(graphene.ID, required=True))

    def resolve_note(self, info, id):
        return NoteType.get_query(info).get(id)


# List of Notes
class QueryNotesList:
    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return NoteType.get_query(info).all()


# Relay of Notes
class QueryNotesRelay:
    notes_relay = SQLAlchemyConnectionField(NoteTypeRelay.connection)
