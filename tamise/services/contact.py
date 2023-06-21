from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from tamise import models, schemas


def get_contact_msgs(db: Session):
    comments = db.query(models.Comment).all()
    return comments


def create_contact_msg(comment_schema: schemas.ContactMsg, db: Session):
    del comment_schema.id  # ignore id
    new_comment = models.Comment(**comment_schema.dict())

    db.add(new_comment)
    db.commit()

    return new_comment.id
