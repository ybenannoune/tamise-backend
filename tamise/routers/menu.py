import json
import pprint

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db
from tamise.services import menu as menu_service

router = APIRouter()


@router.get("/", response_model=schemas.Menu)
async def get_menu(db: Session = Depends(get_db)):
    dishs = db.query(models.Dish).all()
    drinks = db.query(models.Drink).all()
    return {
        "dishs": dishs,
        "drinks": drinks,
    }
