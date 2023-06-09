"""
main.py
"""

from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud
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
    return crud.add_transaction(db, new_transaction)

@app.get("/get_transaction_by_id/{transaction_id}", response_model=List[transaction])
def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    """
    Get a transaction given a transaction_id.
    """
    return crud.get_transaction_by_id(db, transaction_id)

# @app.patch("/update_transaction/{transaction_id}", response_model=transaction)
# def patch_transaction(transaction_id: int, db: Session = Depends(get_db)):
#     """
#     Update a transaction in the table.
#     """
#     return update_transaction(db, new_transaction)
