from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings.get_settings import settings


SQLALCHEMY_DATABASE_URL = "mysql://{}:{}@{}/{}".format(
    settings.DATABASE_USER, settings.DATABASE_PASSWORD, settings.DATABASE_HOST, settings.DATABASE_NAME
)

print("SQLALCHEMY_DATABASE_URL", SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
