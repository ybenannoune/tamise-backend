import uuid
from datetime import datetime
from typing import List

from pydantic import UUID4, BaseModel, EmailStr, constr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    photo: str

    class Config:
        orm_mode = True


class CreateUser(UserBase):
    password: constr(min_length=8)
    role: str = "user"
    verified: bool = False


class LoginUser(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class AuthToken(BaseModel):
    status: str
    access_token: str


class UserResponse(UserBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime


# Dish Schemas


class Dish(BaseModel):
    id: int
    name: str
    category: str
    ingredients: str
    image: str
    description: str
    price: float

    class Config:
        orm_mode = True


class UpdateDish(BaseModel):
    name: str
    category: str
    ingredients: str
    image: str
    description: str
    price: float


class ListDish(BaseModel):
    dishs: List[Dish]
    len: int


# Order Schemas


class OrderResponse(BaseModel):
    order_id: int

    class Config:
        orm_mode = True


class OrderItem(BaseModel):
    dish_id: int
    quantity: int
    modifiers: str
    drink: str


class Order(BaseModel):
    name: str
    phone_number: str
    address: str
    order_items: List[OrderItem]
    delivery_date: datetime
