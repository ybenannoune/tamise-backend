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


# Extra Schemas


class Drink(BaseModel):
    id: int
    name: str
    price: float
    image: str | None
    volume: int

    class Config:
        orm_mode = True


# Dish Schemas


class DishBase(BaseModel):
    name: str
    category: str
    ingredients: str
    image: str
    description: str
    price: float

    class Config:
        orm_mode = True


class Dish(DishBase):
    id: int


class ListDish(BaseModel):
    dishs: List[Dish]


# Order Schemas


class OrderResponse(BaseModel):
    order_id: int

    class Config:
        orm_mode = True


class OrderItem(BaseModel):
    dish_id: int
    drink_id: int | None
    quantity: int
    modifiers: List[str] | None


class OrderBase(BaseModel):
    name: str
    phone_number: str
    address: str
    delivery_date: datetime
    order_items: List[OrderItem]


class Order(OrderBase):
    order_status: str
    order_date: datetime


# Menu Schemas
class Menu(BaseModel):
    dishs: List[Dish]
    drinks: List[Drink]
