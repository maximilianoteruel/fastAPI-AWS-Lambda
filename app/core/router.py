# FastAPI
from fastapi import APIRouter
from app.core.settings import get_settings

# GraphQL
import graphene
from starlette.graphql import GraphQLApp
from app.core.graphql import schema

# Routers
from app.api.rest.notes import router as notes_router
from app.api.rest.users import router as users_router
from app.api.rest.login import router as login_router

core_router = APIRouter()
core_router.include_router(notes_router, prefix="/notes", tags=["notes"])
core_router.include_router(users_router, prefix="/users", tags=["users"])
core_router.include_router(login_router, prefix="/login", tags=["login"])
core_router.add_route("/graphql", GraphQLApp(schema=schema, graphiql=get_settings().GRAPHIQL))
