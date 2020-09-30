# FastAPI

## Environment Variables

```
- TYPE
  Allowed Values: API, TEST
  Description: Used by start script to run different modules, for example api, celery-worker, test, etc (./docker/start.__.sh)

- ENVIRONMENT
  Allowed Values: DEV, PROD
  Description: Used by the application to change internal settings (./app/core/settings)


- DATABASE_HOST
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_NAME
```

## Run Development Environment

- Install docker and docker-compose
- Run in terminal:

```bash
docker-compose -f "docker-compose.yml" up -d --build
```

**Database** will be exposed on port **3306**
**API** will be exposed on port **8000**

## Run Tests

- Run in terminal:

```bash
docker-compose -f "docker-compose.test.yml" up -d --build
```

Check the results in **test** container logs

## Main Dependencies

- _SQLAlchemy_: ORM
- _Alembic_: Database Migrations
- _Graphene_: GraphQL

## Files Structure

```bash
- ./alembic/versions #database migrations

- ./docker #contains files needed in Dockerfile
- ./docker/requirements #python dependencies
- ./docker/scripts/entrypoint.sh #script to run in docker ENTRYPOINT
- ./docker/scripts/start.dev.sh #script to run in docker CMD (only in dev environment)
- ./docker/scripts/start.prod.sh #script to run in docker CMD (only in prod environment)

- ./app/core #core files common to the entire app, like db conection, settings configurations, etc...

- ./app/models #SQLAlchemy models (database)
- ./app/schemas #Pydantic models (data shape)
- ./app/cruds #Classes to manipulate the Models

- ./app/tests #tests

- ./app/api #api REST and GraphQL fucionalities
```
