from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"data": "blog list"}

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str]=None):
    # return published
    if published:
        return {"data": f"{limit} blogs from the list"}
    else:
        return {"data": f"{limit} blogs from the db"}

@app.get("/block/unpublished")
def about():
    return {"data": "all unpublished blog"}

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # return limit
    return {"data": {"1", "2"}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    # return blog
    return {"data": f"{blog.title} is created"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

# uvicorn main:app --reload
