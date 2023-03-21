"""
main.py
"""

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .crud import add_transaction
from .database import SessionLocal, engine
from .models import Base
from .schemas import transaction


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    """
    Get db dependecy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/add_transaction/", response_model=transaction)
def post_transaction(new_transaction: transaction, db: Session = Depends(get_db)):
    """
    Add new transaction to table.
    """
    return add_transaction(db, new_transaction)
