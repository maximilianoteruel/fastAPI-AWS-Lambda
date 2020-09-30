# FastAPI
from fastapi import APIRouter
from app.core.settings.get_settings import settings

# GraphQL
import graphene
from starlette.graphql import GraphQLApp
from app.core.graphql import schema

# Routers
from app.api.router import api_router

core_router = APIRouter()
core_router.include_router(api_router)
core_router.add_route("/graphql", GraphQLApp(schema=schema, graphiql=settings.GRAPHIQL))
