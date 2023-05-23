# routers/order.py

import tamise.services.order as order_service
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from tamise.database import get_db
from tamise.schemas import CreateOrder, Order

router = APIRouter()


@router.post("/create", response_model=Order)
async def create_order(order: CreateOrder, db: Session = Depends(get_db)):
    order_id = order_service.create_order(db, order)
    return Order(order_id=order_id)
