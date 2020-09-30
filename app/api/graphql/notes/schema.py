# GraphQL
import graphene

# Queries & Mutations
from .query import *
from .mutation import *


class Query(
    QueryNote, QueryNotesList, QueryNotesRelay, graphene.ObjectType,
):
    pass


class Mutation(graphene.ObjectType):
    note_create = NoteCreate.Field()
    note_update = NoteUpdate.Field()
    note_delete = NoteDelete.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
