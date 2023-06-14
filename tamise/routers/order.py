# routers/order.py

from typing import List

import tamise.services.order as order_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tamise import models, oauth2, schemas
from tamise.database import get_db
from tamise.schemas import Order, OrderBase, OrderResponse

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create_order(order: OrderBase, db: Session = Depends(get_db)):
    order_id = order_service.create_order(db, order)
    return OrderResponse(order_id=order_id)


@router.get("/", response_model=List[Order])
def get_orders(db: Session = Depends(get_db), user_id: str = Depends(oauth2.require_user)):
    orders = order_service.get_all_orders(db)
    return orders
