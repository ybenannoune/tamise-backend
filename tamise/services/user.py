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
    user = user_service.get_user_from_email(user_schema.email, db)
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Account already exist")

    #  Hash the password
    user.password = utils.hash_password(user.password)

    user.role = "user"
    user.verified = True
    user.email = EmailStr(user.email.lower())
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()

    return new_user
