from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db
from tamise.services import user as user_service

router = APIRouter()


@router.get("/me", response_model=schemas.UserResponse)
def get_me(db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    return user_service.get_user_from_id(user_id, db)
