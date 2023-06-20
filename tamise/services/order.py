from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from tamise import models, schemas


def create_order(db: Session, order: schemas.OrderBase):
    new_order = models.Order(
        name=order.name,
        delivery_date=order.delivery_date,
        address=order.address,
        phone_number=order.phone_number,
    )

    db.add(new_order)
    db.commit()

    order_items = [
        models.OrderItem(
            order_id=new_order.id,
            dish_id=item.dish_id,
            quantity=item.quantity,
            modifiers=", ".join(item.modifiers),
            drink_id=item.drink_id,
        )
        for item in order.order_items
    ]
    db.bulk_save_objects(order_items)  # un seul call à la db plutôt que plein de petits calls
    db.commit()

    return new_order.id


def get_all_orders(db: Session):
    # Requête pour récupérer les commandes avec les éléments de commande associés
    query = (
        db.query(models.Order, models.OrderItem)
        .join(models.OrderItem, models.Order.id == models.OrderItem.order_id)
        .all()
    )

    # Dictionnaire pour stocker les commandes fusionnées
    merged_orders = {}

    # Parcourir les résultats de la requête
    for order, order_item in query:
        # Vérifier si la commande a déjà été ajoutée au dictionnaire
        if order.id not in merged_orders:
            # Créer un objet OrderResponse pour stocker les données fusionnées
            merged_order = schemas.Order(
                id=order.id,
                name=order.name,
                phone_number=order.phone_number,
                address=order.address,
                order_items=[],
                delivery_date=order.delivery_date,
                order_date=order.order_date,
                order_status=order.status,
            )
            merged_orders[order.id] = merged_order

        if order_item != None:
            # Créer un objet CartItem pour chaque élément de commande
            orderItem = schemas.OrderItem(
                dish_id=order_item.dish_id,
                quantity=order_item.quantity,
                modifiers=order_item.modifiers.split(", "),
                drink_id=order_item.drink_id,
            )
            merged_orders[order.id].order_items.append(orderItem)

    # Retourner la liste des commandes fusionnées
    return list(merged_orders.values())


def update_order_status(id: int, new_status: schemas.Status, db: Session, user_id: str):
    order = db.query(models.Order).filter(models.Order.id == id).first()

    if not order:
        raise HTTPException(
            status_code=status.HTTP_200_OK, detail=f"No order with this id: {id} found"
        )

    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not allowed to perform this action",
        )

    order.status = new_status.status
    db.commit()
