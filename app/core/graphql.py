# GraphQL
import graphene

# Schemas
from app.api.graphql import schema

from app.core.db.session import ScopedSession

# from sqlalchemy.orm import scoped_session


class Query(
    schema.Query, graphene.ObjectType,
):
    pass


# class Mutation(
#     schema.Mutation, graphene.ObjectType,
# ):
#     pass


schema = graphene.Schema(query=Query)

# schema = graphene.Schema(query=Query, mutation=Mutation)
