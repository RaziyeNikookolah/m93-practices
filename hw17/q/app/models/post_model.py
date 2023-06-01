from pydantic import Field, BaseModel


class PostSchema(BaseModel):
    title: str = Field(default=None)
    content: str = Field(default=None)
    author: str = Field(default=None)

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "post_schema": {
    #                 "title": "Hiro",
    #                 "content": "Hiro description",
    #                 "author": "raziye",
    #             }
    #         }
    #     }
