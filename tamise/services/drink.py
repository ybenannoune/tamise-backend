from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from tamise import models


def get_all_drinks(db: Session):
    drinks = db.query(models.Drink).all()
    return drinks
