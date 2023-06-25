# routers/order.py

from typing import List

import tamise.services.order as order_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.CreatedID)
async def create_order(order: schemas.NewOrder, db: Session = Depends(get_db)):
    order_id = order_service.create_order(db, order)
    return schemas.CreatedID(id=order_id)


@router.get("/", response_model=List[schemas.Order])
async def get_orders(
    db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)
):
    orders = order_service.get_all_orders(db)
    return orders


@router.put("/{id}")
async def update_order_status(
    id: int,
    status: schemas.UpdatedStatus,
    db: Session = Depends(get_db),
    user_id: str = Depends(oauth2.require_user),
):
    order_service.update_order_status(id, status, db, user_id)
    return {"status": "success"}
