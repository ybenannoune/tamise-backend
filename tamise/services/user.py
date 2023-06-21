from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session
from tamise import models, schemas, utils
from tamise.services import user as user_service


def get_user_from_id(user_id: str, db: Session):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_from_email(email: str, db: Session):
    return db.query(models.User).filter(models.User.email == EmailStr(email.lower())).first()


def create(user_schema: schemas.CreateUser, db: Session):
    user_check = user_service.get_user_from_email(user_schema.email, db)
    if user_check:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exist")

    #  Hash the password
    user_schema.password = utils.hash_password(user_schema.password)

    user_schema.role = "user"
    user_schema.verified = False
    user_schema.email = EmailStr(user_schema.email.lower())
    new_user = models.User(**user_schema.dict())

    db.add(new_user)
    db.commit()

    return new_user
