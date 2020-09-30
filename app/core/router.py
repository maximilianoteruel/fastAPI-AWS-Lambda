# FastAPI
from fastapi import APIRouter
from app.core.settings import get_settings

# GraphQL
import graphene
from starlette.graphql import GraphQLApp
from app.core.graphql import schema

# Routers
from app.api.rest.notes import router as notes_router

core_router = APIRouter()
core_router.include_router(notes_router, prefix="/notes", tags=["notes"])
core_router.add_route("/graphql", GraphQLApp(schema=schema, graphiql=get_settings().GRAPHIQL))
