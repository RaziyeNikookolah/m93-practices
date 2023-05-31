from pydantic import Field, BaseModel, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "post_schema": {"title": "some title", "content": "description"}
            }
        }


class UserSchema(BaseModel):
    id: int = Field(default=None)  # it can be ... in paranthesese
    fullname: int = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema_extra = {
            "example": {
                "user_schema": {
                    "fullname": "raziye nikookolah",
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
