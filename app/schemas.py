from pydantic import BaseModel, Field

class PostCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    content: str = Field(min_length=1)

class PostUpdate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    content: str = Field(min_length=1)
