from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .database import Base
from sqlalchemy.orm import relationship

blog_tag = Table(
    'blog_tag',
    Base.metadata,
    Column('blog_id', Integer, ForeignKey('blogs.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    blogs = relationship("Blog", secondary=blog_tag, back_populates="tags")  # Many-to-Many

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")  # Define relationship with User
    tags = relationship("Tag", secondary=blog_tag, back_populates="blogs")  # Many-to-Many

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    bio = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)  # One-to-One
    user = relationship("User", back_populates="profile")  # One-to-One

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blogs = relationship("Blog", back_populates="creator")  # Allows access to User's blogs One-to-Many
    profile = relationship("Profile", back_populates="user", uselist=False)  # One-to-One