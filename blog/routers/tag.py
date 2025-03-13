from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database
from typing import List

router = APIRouter(
    prefix="/tag",
    tags=["Tags"]
)
get_db = database.get_db

@router.post("/", response_model=schemas.Tag)
def create_tag(request: schemas.TagCreate, db: Session = Depends(get_db)):
    new_tag = models.Tag(name=request.name)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@router.get("/", response_model=List[schemas.Tag])
def get_all_tags(db: Session = Depends(get_db)):
    tags = db.query(models.Tag).all()
    return tags

@router.get("/{id}", response_model=schemas.Tag)
def get_tag(id: int, db: Session = Depends(get_db)):
    tag = db.query(models.Tag).filter(models.Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tag not found")
    return tag