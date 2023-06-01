from pydantic import Field, BaseModel, EmailStr
from enum import Enum


class UserSchema(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "user_schema": {
    #                 "username": "raziye nikookolah",
    #                 "email": "r.nikookolah@gmail.com",
    #                 "password": "123",
    #             }
    #         }
    #     }


class UserRole(Enum):
    REGULAR = "regular"
    ADMIN = "admin"


class UserLoginSchema(BaseModel):
    username: str = Field(default=None)
    password: str = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         "user_schema": {
    #             "email": "r.nikookolah@gmail.com",
    #             "password": "123",
    #         }
    #     }
