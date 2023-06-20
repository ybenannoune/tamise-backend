from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import EmailStr
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas, utils
from tamise.database import get_db
from tamise.services import auth as auth_service
from tamise.services import user as user_service

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.UserResponse,
)
def create_user(payload: schemas.CreateUser, db: Session = Depends(get_db)):
    user = user_service.create(payload, db)
    return user


@router.post("/login", status_code=status.HTTP_200_OK, response_model=schemas.AuthToken)
def login(
    payload: schemas.LoginUser,
    response: Response,
    db: Session = Depends(get_db),
    authorize: AuthJWT = Depends(),
):
    access_token, refresh_token = auth_service.login(payload, response, db, authorize)

    return {"status": "success", "access_token": access_token, "refresh_token": refresh_token}


# Refresh access token
@router.post("/refresh", response_model=schemas.AccessToken)
def refresh_token(
    response: Response,
    authorize: AuthJWT = Depends(),
    db: Session = Depends(get_db),
):
    access_token = auth_service.refresh(response, authorize, db)
    return {"status": "success", "access_token": access_token}


@router.post("/logout", status_code=status.HTTP_200_OK)
def logout(
    request: Request,
    response: Response,
    authorize: AuthJWT = Depends(),
    user_id: str = Depends(oauth2.require_user),
):
    authorize.unset_jwt_cookies()
    response.set_cookie("logged_in", "", -1)
    return {"status": "success"}
