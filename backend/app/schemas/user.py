# from pydantic import BaseModel, EmailStr
# from typing import Optional


# class UserBase(BaseModel):
#     email: EmailStr

# # class UserCreate(UserBase):
# #     password: str
# #     role_id: int

# class UserCreate(BaseModel):
#     username: Optional[str] = None
#     email: EmailStr
#     password: str
#     # role_id: int
#     is_superuser: Optional[bool] = False  # default to False
#     role_id: Optional[int] = None         # Optional, validated in endpoint logic


# # class UserLogin(BaseModel):  # This was missing
# #     email: EmailStr
# #     password: 


# class LoginRequest(BaseModel):
#     email: str
#     password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class UserUpdate(BaseModel):
#     email: Optional[EmailStr] = None
#     password: Optional[str] = None
#     is_active: Optional[bool] = None

# class UserOut(UserBase):
#     id: int
#     is_active: bool
    
#     class Config:
#         from_attributes = True  # Replaces orm_mode in Pydantic v2

# class TokenResponse(BaseModel):
#     access_token: str
#     refresh_token: str
#     token_type: str

# class TokenData(BaseModel):
#     user_id: int | None = None
#     token_type: str | None = None


# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
from app.schemas.base import TimeStampSchema  # ✅ Import TimeStampSchema


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str] = None


class UserCreate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)
    role_id: Optional[int] = None
    is_superuser: Optional[bool] = False
    
    class Config:
        extra = "forbid"


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    role_id: Optional[int] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    
    class Config:
        extra = "forbid"


class UserOut(UserBase, TimeStampSchema):  # ✅ Now includes created_at, updated_at, deleted, deleted_at
    id: int
    is_active: bool
    is_superuser: bool
    role_id: Optional[int] = None
    employee_id: Optional[int] = None
    
    class Config:
        from_attributes = True


class PaginatedUsers(BaseModel):
    count: int
    data: list[UserOut]


class UserListResponse(BaseModel):
    status: str
    result: PaginatedUsers


# Auth schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None
    token_type: Optional[str] = None