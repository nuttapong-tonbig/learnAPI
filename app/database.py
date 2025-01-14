from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("postgresql://dbtest_l33d_user:smFcb1jw9awubGg8dAlyMbsqUtkmbvjq@dpg-cu2vcvtds78s73ectdqg-a/dbtest_l33d")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
