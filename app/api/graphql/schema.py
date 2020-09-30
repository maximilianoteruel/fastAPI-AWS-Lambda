# GraphQL
import graphene

# Queries & Mutations
from .query import *
from .mutation import *


class Query(
    QueryNote, graphene.ObjectType,
):
    pass


class Mutation(graphene.ObjectType):
    pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
