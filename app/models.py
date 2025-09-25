from pydantic import BaseModel, Field

class Post(BaseModel):
    id: int
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    content: str = Field(min_length=1)
