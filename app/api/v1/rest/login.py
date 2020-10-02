from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.cruds import users as cruds
from app.models import users as models
from app.schemas import users as schemas_user
from app.schemas import token as schemas_token
from app.api import deps
from app.core import security
from app.core.settings import get_settings
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/access-token", response_model=schemas_token.Token)
def login_access_token(
    db: Session = Depends(deps.get_db_local), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = cruds.user.authenticate(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not cruds.user.is_active(user):
        raise HTTPException(status_code=400, detail="Inactive user")
    access_token_expires = timedelta(minutes=get_settings().JWT_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }


@router.post("/test-token", response_model=schemas_user.User)
def test_token(current_user: models.User = Depends(deps.get_current_user)) -> Any:
    """
    Test access token
    """
    return current_user
