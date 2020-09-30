# GraphQL
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

# Models
from app.models.notes import Note


class NoteType(SQLAlchemyObjectType):
    class Meta:
        model = Note


class NoteTypeRelay(SQLAlchemyObjectType):
    class Meta:
        model = Note
        interfaces = (relay.Node,)


class QueryNote:
    # Note by ID
    note = graphene.Field(NoteType, id=graphene.Argument(graphene.ID, required=True))

    def resolve_note(self, info, id):
        return NoteType.get_query(info).get(id)

    # List of Notes
    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return NoteType.get_query(info).all()

    # Relay of Notes
    notes_relay = SQLAlchemyConnectionField(NoteTypeRelay.connection)
