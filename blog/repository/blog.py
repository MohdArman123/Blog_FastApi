from sqlalchemy.orm import Session, joinedload
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(models.Blog).options(joinedload(models.Blog.tags)).all()
    # blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session, user_id: int):
    tags = db.query(models.Tag).filter(models.Tag.id.in_(request.tag_ids)).all()
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user_id, tags=tags)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id: int, request:schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Blog with id {id} not found")
    blog.update(request.dict())
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    blog = db.query(models.Blog).options(joinedload(models.Blog.tags)).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog