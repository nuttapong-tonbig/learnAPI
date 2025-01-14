from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Item

router = APIRouter()

@router.get("/items/")
def read_items(db: Session = Depends(get_db)):
    items = db.query(Item).all()
    return items
