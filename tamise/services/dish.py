from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from tamise import models


def get_dish_from_id(id: int, db: Session):
    return db.query(models.Dish).filter(models.Dish.id == id).first()


def get_all_dishs(db: Session):
    dishs = db.query(models.Dish).all()
    return dishs


# def update_dish(id: int, dish: models.NewDish, db: Session, user_id: str):
#     if id <= 0:
#         raise ValueError("Invalid dish ID")

#     dish_to_update = get_dish_from_id(id, db)

#     if not dish_to_update:
#         raise HTTPException(
#             status_code=status.HTTP_200_OK, detail=f"No dish with this id: {id} found"
#         )
#     if not user_id:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="You are not allowed to perform this action",
#         )

#     db.query(models.Dish).filter(models.Dish.id == id).update(
#         dish.dict(exclude_unset=True), synchronize_session=False
#     )
#     db.commit()
#     return dish_to_update
