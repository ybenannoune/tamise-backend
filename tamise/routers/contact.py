# routers/comment.py

from typing import List

import tamise.services.contact as comment_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db
from tamise.schemas import IdBase, Order, OrderBase

router = APIRouter()


@router.post("/", response_model=IdBase)
async def create_contact_msg(comment: schemas.ContactMsg, db: Session = Depends(get_db)):
    comment_id = comment_service.create_contact_msg(comment, db)
    return IdBase(id=comment_id)


@router.get("/", response_model=List[schemas.ContactMsg])
async def get_contact_msgs(
    db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)
):
    comments = comment_service.get_all_comments(db)
    return comments
