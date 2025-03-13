from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, models, database, oauth2

router = APIRouter(
    prefix="/profile",
    tags=["Profiles"]
)

get_db = database.get_db

@router.post("/", response_model=schemas.Profile)
def create_profile(request: schemas.ProfileCreate, db: Session = Depends(get_db), current_user: models.User =Depends(oauth2.get_current_user)
):
    if request.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    # Check if a profile already exists for the current user
    existing_profile = db.query(models.Profile).filter(models.Profile.user_id == current_user.id).first()
    if existing_profile:
        raise HTTPException(status_code=400, detail="Profile for this user already exists")
    new_profile = models.Profile(**request.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    return new_profile

@router.get("/{user_id}", response_model=schemas.Profile)
def get_profile(user_id: int, db: Session = Depends(get_db)):
    profile = db.query(models.Profile).filter(models.Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profile not found")
    return profile
    