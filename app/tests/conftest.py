from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.db.session import session_local
from app.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield session_local()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
