# GraphQL
import graphene

# Schemas
from app.api.graphql import notes

from app.core.db.session import ScopedSession

# from sqlalchemy.orm import scoped_session


class Query(
    notes.schema.Query, graphene.ObjectType,
):
    pass


class Mutation(
    notes.schema.Mutation, graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
