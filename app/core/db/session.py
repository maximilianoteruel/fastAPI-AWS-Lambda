from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.core.settings import get_settings


SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}/{}".format(
    get_settings().DATABASE_USER,
    get_settings().DATABASE_PASSWORD,
    get_settings().DATABASE_HOST,
    get_settings().DATABASE_NAME,
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
ScopedSession = scoped_session(SessionLocal)
