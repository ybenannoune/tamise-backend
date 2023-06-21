import uuid
from datetime import datetime
from typing import List

from pydantic import UUID4, BaseModel, EmailStr, constr


class IdBase(BaseModel):
    id: int

    class Config:
        orm_mode = True


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


class AccessToken(BaseModel):
    status: str
    access_token: str


class AuthToken(BaseModel):
    status: str
    access_token: str
    refresh_token: str


class UserResponse(UserBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime


# Comment Schemas


class ContactMsg(IdBase):
    name: str
    email: str
    message: str


# Extra Schemas


class Drink(IdBase):
    name: str
    price: float | None
    image: str | None
    volume: int | None
    description: str | None


# Dish Schemas


class Dish(IdBase):
    name: str
    category: str
    ingredients: str
    removable_ingredients: str | None
    image: str
    description: str
    price: float
    customizable_dish: bool

    class Config:
        orm_mode = True


class ListDish(BaseModel):
    dishs: List[Dish]


# Order Schemas


class OrderItem(BaseModel):
    dish_id: int
    drink_id: int | None
    quantity: int
    modifiers: List[str] | None


class OrderBase(IdBase):
    name: str
    phone_number: str
    address: str
    delivery_date: datetime
    order_items: List[OrderItem]


class Order(OrderBase):
    order_status: str
    order_date: datetime


class Status(BaseModel):
    status: str


# Menu Schemas
class Menu(BaseModel):
    dishs: List[Dish]
    drinks: List[Drink]
