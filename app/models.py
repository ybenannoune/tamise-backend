import uuid
from .database import Base, engine
from sqlalchemy import ForeignKey, Table, TIMESTAMP, Column, String, Boolean,Integer, Float, DateTime, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

# Used for Administration
class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    photo = Column(String, nullable=True)
    verified = Column(Boolean, nullable=False, server_default='False')
    role = Column(String, server_default='user', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))

# Table Dish
class Dish(Base):
    __tablename__ = 'dishes'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    image = Column(String, nullable=True)
    category = Column(String, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)

# Table Order
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_date = Column(DateTime, nullable=False)
    delivery_date = Column(DateTime, nullable=False)
    name = Column(String, nullable=True)
    address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)

# # Table to connect order and dish
# orders_dishes = Table('orders_dishes', Base.metadata,
#                       Column('order_id', Integer, ForeignKey('orders.id')),
#                       Column('dish_id', Integer, ForeignKey('dishes.id')),
#                       Column('quantity', Integer, nullable=False),
#                       Column('supplement', String, nullable=True),
#                       Column('modifications', String, nullable=True))

Base.metadata.create_all(engine)