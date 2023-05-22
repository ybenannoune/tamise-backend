from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models, schemas
from ..database import get_db

router = APIRouter()

# {
#   "name": "DUPONT",
#   "phone_number": "010203040506",
#   "address": "Avenue General Leclerc",
#   "cartItems": [
#     {
#       "dishId": 1,
#       "quantity": 4,
#       "modifier": "-piment",
#       "drink": "Coca"
#     },
#     {
#       "dishId": 1,
#       "quantity": 2,
#       "modifier": "-harissa",
#       "drink": "Fanta"
#     }
#   ],
#   "delivery_date": "2023-05-22T22:25:39.779Z"
# }

@router.post("/create")
async def create_order(payload: schemas.CreateOrderSchema, db: Session = Depends(get_db)):

    print(payload)

    order = models.Order(
        order_date=datetime.utcnow(),
        delivery_date=payload.delivery_date,
        address=payload.address,
        phone_number=payload.phone_number
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    for item in payload.cartItems:
        # dish = db.query(models.Dish).get(item.dishId)
        order_item = models.OrderItems(
            order_id=order.id,
            dish_id=item.dishId,
            quantity=item.quantity,
            modifiers=item.modifier,
            drink=item.drink
        )
        db.add(order_item)

    db.commit()

    return {"order_id": order.id}