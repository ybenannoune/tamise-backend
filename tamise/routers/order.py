# routers/order.py

from typing import List

import tamise.services.order as order_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tamise.database import get_db
from tamise.schemas import Order, OrderResponse

router = APIRouter()


@router.post("/", response_model=OrderResponse)
def create_order(order: Order, db: Session = Depends(get_db)):
    order_id = order_service.create_order(db, order)
    return OrderResponse(order_id=order_id)


@router.get("/", response_model=List[Order])
def get_orders(db: Session = Depends(get_db)):
    orders = order_service.get_all_orders(db)
    return orders
