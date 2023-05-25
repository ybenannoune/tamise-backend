from datetime import datetime

from sqlalchemy.orm import Session
from tamise import models, schemas


def create_order(db: Session, order: schemas.Order):
    new_order = models.Order(
        name=order.name,
        delivery_date=order.delivery_date,
        address=order.address,
        phone_number=order.phone_number,
    )

    db.add(new_order)
    db.commit()

    cart_items = [
        models.OrderItem(
            order_id=new_order.id,
            dish_id=item.dish_id,
            quantity=item.quantity,
            modifiers=item.modifiers,
            drink=item.drink,
        )
        for item in order.order_items
    ]
    db.bulk_save_objects(
        cart_items
    )  # un seul call à la db plutôt que plein de petits calls
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
                order_id=order.id,
                name=order.name,
                phone_number=order.phone_number,
                address=order.address,
                order_items=[],
                delivery_date=order.delivery_date,
            )
            merged_orders[order.id] = merged_order

        # Créer un objet CartItem pour chaque élément de commande
        cart_item = schemas.OrderItem(
            dish_id=order_item.dish_id,
            quantity=order_item.quantity,
            modifiers=order_item.modifiers,
            drink=order_item.drink,
        )
        merged_orders[order.id].order_items.append(cart_item)

    # Retourner la liste des commandes fusionnées
    return list(merged_orders.values())
