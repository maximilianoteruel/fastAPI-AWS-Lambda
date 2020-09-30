# GraphQL
import graphene

# Core
from app.core.db.session import SessionScoped

# Models
from app.models.notes import Note

# Types
from .types import NoteType

# Cruds
from app.cruds.notes import crud_note


# Create Note
class NoteCreate(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        tags = graphene.String(required=True)

    data = graphene.Field(NoteType)
    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, **kwargs):
        data = crud_note.create(db=SessionScoped, obj_in=kwargs)
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
        note = crud_note.get(db=SessionScoped, id=kwargs["id"])
        if note is None:
            return NoteUpdate(status=False, data=None)
        data = crud_note.update(db=SessionScoped, db_obj=note, obj_in=kwargs)
        return NoteUpdate(status=True, data=data)


# Delete Note
class NoteDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.Field(graphene.Boolean)

    def mutate(self, info, **kwargs):
        note = crud_note.get(db=SessionScoped, id=kwargs["id"])
        if note is None:
            return NoteDelete(status=False)
        data = crud_note.remove(db=SessionScoped, id=note.id)
        return NoteDelete(status=True)
