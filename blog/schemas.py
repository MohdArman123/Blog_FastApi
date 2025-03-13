from typing import List
from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str
    tag_ids: List[int] = []
    # user_id: int

class Blog(BlogBase):
    class Config():
        from_attributes = True

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    blogs: List[Blog] = []  # Use the class directly now
    class Config:
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    tags: List[Tag] = []
    class Config():
        from_attributes = True
    

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

class ProfileBase(BaseModel):
    bio: str

class ProfileCreate(ProfileBase):
    user_id: int

class Profile(ProfileBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True