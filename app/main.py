from fastapi import FastAPI, HTTPException, status
from typing import List

from . import models, schemas, storage

app = FastAPI()

@app.post("/posts", response_model=models.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate):
    global next_id
    new_post = models.Post(id=storage.next_id, **post.dict())
    storage.posts[storage.next_id] = new_post
    storage.next_id += 1
    return new_post

@app.get("/posts", response_model=List[models.Post])
def get_posts():
    return list(storage.posts.values())

@app.get("/posts/{id}", response_model=models.Post)
def get_post(id: int):
    if id not in storage.posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return storage.posts[id]

@app.put("/posts/{id}", response_model=models.Post)
def update_post(id: int, post: schemas.PostUpdate):
    if id not in storage.posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    updated_post = models.Post(id=id, **post.dict())
    storage.posts[id] = updated_post
    return updated_post

@app.delete("/posts/{id}")
def delete_post(id: int):
    if id not in storage.posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    del storage.posts[id]
    return {"message": "Post deleted successfully"}
