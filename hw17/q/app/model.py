from pydantic import Field, BaseModel, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)
    author: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "post_schema": {
                    "title": "Hiro",
                    "content": "Hiro description",
                    "author": "raziye",
                }
            }
        }


class UserSchema(BaseModel):
    id: int = Field(default=None)  # it can be ... in paranthesese
    username: int = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "user_schema": {
                    "username": "raziye nikookolah",
                    "email": "r.nikookolah@gmail.com",
                    "password": "123",
                }
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "user_schema": {
                "email": "r.nikookolah@gmail.com",
                "password": "123",
            }
        }
