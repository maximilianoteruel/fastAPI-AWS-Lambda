# FastAPI
from fastapi import APIRouter

# GraphQL
import graphene
from starlette.graphql import GraphQLApp
from .graphql.schema import schema

# Routers
from .rest.notes import router as notes_router
from .rest.users import router as users_router
from .rest.login import router as login_router

api_v1_router = APIRouter()
api_v1_router.include_router(notes_router, prefix="/notes", tags=["notes"])
api_v1_router.include_router(users_router, prefix="/users", tags=["users"])
api_v1_router.include_router(login_router, prefix="/login", tags=["login"])
api_v1_router.add_route("/graphql", GraphQLApp(schema=schema, graphiql=True))
