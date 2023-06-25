import uuid

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from tamise.database import Base


# Used for Administration
class User(Base):
    __tablename__ = "user"
    id = Column(
        UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4
    )
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default="False")
    role = Column(String, server_default="user", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


# Table Dish
class Dish(Base):
    __tablename__ = "dish"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    removable_ingredients = Column(String, nullable=True)
    image = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    customizable_dish = Column(Boolean, nullable=True)


class Drink(Base):
    __tablename__ = "drink"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=True)
    image = Column(String, nullable=True)
    volume = Column(Integer, nullable=False)
    description = Column(String, nullable=True)


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    message = Column(String, nullable=False)


# Table Order
class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=True, server_default=func.now())
    delivery_date = Column(DateTime, nullable=False)
    name = Column(String, nullable=True)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    status = Column(String, server_default="Commandé", nullable=True)


class OrderItem(Base):
    __tablename__ = "order_item"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    dish_id = Column(Integer, ForeignKey("dish.id"))
    drink_id = Column(Integer, ForeignKey("drink.id"), nullable=True)
    quantity = Column(Integer, nullable=False)
    modifiers = Column(String, nullable=True)

    order = relationship(Order, foreign_keys=[order_id])
    dish = relationship(Dish, foreign_keys=[dish_id])
    drink = relationship(Drink, foreign_keys=[drink_id])
