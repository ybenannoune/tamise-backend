from datetime import datetime
import uuid
from pydantic import BaseModel, EmailStr, constr
from typing import List

class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    photo: str

    class Config:
        orm_mode = True

class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    role: str = 'user'
    verified: bool = False

class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class UserResponse(UserBaseSchema):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime



class Ingredient(BaseModel):
    name: str
    quantity: int

class Dish(BaseModel):
    id: int
    name: str
    category: str
    ingredients: List[Ingredient]
    image: str
    description: str
    price: float    

class CartItem(BaseModel):
    id: int
    dishItem: Dish
    quantity: int
    modifier: List[str]
    drink: str

class User(BaseModel):
    name: str
    tel: str
    address: str

class CreateOrderSchema(BaseModel):
    user: User
    cartItems: List[CartItem]
    delivery_date: datetime
