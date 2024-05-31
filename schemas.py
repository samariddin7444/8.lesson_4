from pydantic import BaseModel
from typing import Optional


class Registration(BaseModel):
    id: Optional[int]
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "first_name": "Sarvar",
                "last_name": "Fayziyev",
                "username": "Fayziyev9059",
                "email": "fayziyev@gmail.com",
                "password": "****",
                "is_active": True,
                "is_staff": True
            }
        }


class Login(BaseModel):
    username: str
    password: str


class CategoryM(BaseModel):
    id: Optional[int]
    name: str


class ProductM(BaseModel):
    id: Optional[int]
    name: str
    description: str
    price: float
    category_id: Optional[int]


class OrderM(BaseModel):
    id: Optional[int]
    user_id: int
    product_id: int
