from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from tamise import models


def get_all_menu(db: Session):
    query = db.query(models.Dish, models.Drink).all()
    dishes, drinks = query
    return dishes, drinks
