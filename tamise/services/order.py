from datetime import datetime

from sqlalchemy.orm import Session
from tamise import models, schemas


def create_order(db: Session, order: schemas.CreateOrder):
    order = models.Order(   
        name=order.name,
        delivery_date=order.delivery_date,
        address=order.address,
        phone_number=order.phone_number
    )

    db.add(order)
    db.commit()

    cart_items = [
        models.OrderItems(
            order_id=order.id,
            dish_id=item.dishId,
            quantity=item.quantity,
            modifiers=item.modifier,
            drink=item.drink
        ) for item in order.cart_items
    ]
    db.bulk_save_objects(cart_items) # un seul call à la db plutôt que plein de petits calls
    db.commit()

    return order.id