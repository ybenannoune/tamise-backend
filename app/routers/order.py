from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/create")
async def create_order(payload: schemas.CreateOrderSchema, db: Session = Depends(get_db)):

    print(payload)
    
    order = models.Order(
        order_date=datetime.utcnow(),
        delivery_date=payload.delivery_date,
        address=payload.user.address,
        phone_number=payload.user.tel
    )
    
    # TODO ajouter le contenu de la commande dans la DB    

    db.add(order)
    db.commit()
    db.refresh(order)
    
    return {"order_id": order.id}
