from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from app.core.db.session import session_scoped


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    # required by GrahQL
    query = session_scoped.query_property()
