from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

from dotenv import load_dotenv

load_dotenv()  # Load .env variables

# SQLALCHEMY_DATABASE_URL =  "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/blogdb"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
if not SQLALCHEMY_DATABASE_URL:
    raise Exception("DATABASE_URL environment variable not set!")


# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
