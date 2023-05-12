from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/create")
async def create_order(payload: schemas.CreateOrderSchema, db: Session = Depends(get_db)):

    print(payload)

    # Créer l'objet Order
    order = models.Order(
        order_date=datetime.utcnow(),
        delivery_date=payload.delivery_date,
        address=payload.user.address,
        phone_number=payload.user.tel
    )
    
    # Ajouter les plats à la commande
    for item in payload.cart_items:
        dish = db.query(models.Dish).get(item.dish_item.id)
        if dish is None:
            raise HTTPException(status_code=404, detail="Plat non trouvé")
        
        order_item = models.OrderDish(
            quantity=item.quantity,
            supplement=item.drink,
            modifications=", ".join(item.modifier),
            dish=dish
        )
        
        order.dishes.append(order_item)
    
    # Enregistrer la commande en base de données
    db.add(order)
    db.commit()
    db.refresh(order)
    
    return {"order_id": order.id}
