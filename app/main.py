from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import Base, engine, get_db
from app.models import Item

# สร้างตารางในฐานข้อมูล
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic Model สำหรับรับข้อมูลจากผู้ใช้
class ItemCreate(BaseModel):
    name: str
    description: str

@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """
    เพิ่มข้อมูลใหม่ลงในฐานข้อมูล
    """
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)  # อัปเดตข้อมูลหลังจากบันทึกสำเร็จ
    return {"message": "Item created successfully", "item": db_item}

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    """
    ดึงข้อมูลทั้งหมดจากตาราง items
    """
    items = db.query(Item).all()
    return items
