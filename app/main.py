from fastapi import FastAPI
from app.core.router import core_router
from app.core.db.session import SessionScoped

app = FastAPI()
app.include_router(core_router)


@app.on_event("shutdown")
def shutdown_event():
    SessionScoped.remove()
