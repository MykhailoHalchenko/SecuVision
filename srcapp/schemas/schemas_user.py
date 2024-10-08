from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str
    is_superuser: bool = False 

class UserUpdate(UserBase):
    password: Optional[str] = None  
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

class UserOut(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: Optional[str]

    class Config:
        orm_mode = True
