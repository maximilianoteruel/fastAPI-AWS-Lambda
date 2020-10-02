# GraphQL
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

# Types
from app.gql_objects.notes import NoteType, NoteTypeRelay

# Cruds
from app.cruds.notes import crud_note

from app.core.db.session import session_scoped


class Query(graphene.ObjectType):
    #  Note
    note = graphene.Field(NoteType, id=graphene.Argument(graphene.ID, required=True))

    def resolve_note(self, info, id):
        return crud_note.get(db=session_scoped, id=id)

    # List of Notes

    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return crud_note.get_multi(db=session_scoped)

    # Relay of Notes

    notes_relay = SQLAlchemyConnectionField(NoteTypeRelay.connection)


# Create Note
class NoteCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        tags = graphene.String(required=True)

    data = graphene.Field(NoteType)
    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, **kwargs):
        data = crud_note.create(db=session_scoped, obj_in=kwargs)
        return NoteCreate(status=True, data=data)


# Update Note
class NoteUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()
        tags = graphene.String()

    data = graphene.Field(NoteType)
    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, **kwargs):
        note = crud_note.get(db=session_scoped, id=kwargs["id"])
        if note is None:
            return NoteUpdate(status=False, data=None)
        data = crud_note.update(db=session_scoped, db_obj=note, obj_in=kwargs)
        return NoteUpdate(status=True, data=data)


# Delete Note
class NoteDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, **kwargs):
        note = crud_note.get(db=session_scoped, id=kwargs["id"])
        if note is None:
            return NoteDelete(status=False)
        data = crud_note.remove(db=session_scoped, id=note.id)
        return NoteDelete(status=True)


class Mutation(graphene.ObjectType):
    note_create = NoteCreate.Field()
    note_update = NoteUpdate.Field()
    note_delete = NoteDelete.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
