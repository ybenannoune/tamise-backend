from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db
from tamise.services import dish as dish_service

router = APIRouter()


@router.get("/", response_model=schemas.ListDish)
async def get_dishs(db: Session = Depends(get_db)):
    dishs = dish_service.get_all_dishs(db)
    return {"dishs": dishs}


@router.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.Dish)
async def update_dish(
    id: int,
    dish: schemas.Dish,
    db: Session = Depends(get_db),
    user_id: str = Depends(oauth2.require_user),
):
    return dish_service.update_dish(id, dish, db, user_id)
