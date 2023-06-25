import uuid
from datetime import datetime
from typing import List

from pydantic import UUID4, BaseModel, EmailStr, constr


class CreatedID(BaseModel):
    id: int


class NewUser(BaseModel):
    name: str
    email: EmailStr
    photo: str
    password: constr(min_length=8)
    role: str = "user"

    class Config:
        orm_mode = True


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


class User(BaseModel):
    id: UUID4
    name: str
    email: str
    photo: str
    role: str

    class Config:
        orm_mode = True


# Comment Schemas


class NewContactMsg(BaseModel):
    name: str
    email: str
    message: str


class ContactMsg(BaseModel):
    id: str
    name: str
    email: str
    message: str

    class Config:
        orm_mode = True


# Extra Schemas


class Drink(BaseModel):
    id: str
    name: str
    price: float | None
    image: str | None
    volume: int | None
    description: str | None

    class Config:
        orm_mode = True


# Dish Schemas


class Dish(BaseModel):
    id: int
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


class NewOrder(BaseModel):
    name: str
    phone_number: str
    address: str
    delivery_date: datetime
    order_items: List[OrderItem]


class Order(BaseModel):
    id: str
    name: str
    phone_number: str
    address: str
    delivery_date: datetime
    order_items: List[OrderItem]
    order_status: str
    order_date: datetime

    class Config:
        orm_mode = True


class UpdatedStatus(BaseModel):
    status: str


# Menu Schemas
class Menu(BaseModel):
    dishes: List[Dish]
    drinks: List[Drink]
