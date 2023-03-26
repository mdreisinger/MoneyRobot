"""
main.py
"""

from fastapi import Depends, FastAPI
import MySQLdb
from sqlalchemy.orm import Session

from . import crud
from .database import create_engine_session
from .models import Base
from .schemas import transaction


engine, SessionLocal = create_engine_session()

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    """
    Get db dependecy
    """
    _, db = create_engine_session()
    try:
        yield db
    finally:
        #pylint:disable=no-member
        db.close()

@app.post("/add_transaction/", response_model=transaction)
def add_transaction(new_transaction: transaction, db: Session = Depends(get_db)):
    """
    Add new transaction to table.
    """
    try:
        return crud.add_transaction(db, new_transaction)
    except MySQLdb.OperationalError as error:
        print(f"Caught MySQLdb exception: {error}")
        print("Attempting to reconnect to DB and re-try operation")
        db = get_db()
        return crud.add_transaction(db, new_transaction)


# @app.get("/get_transaction_by_id/{transaction_id}", response_model=List[transaction])
# def get_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
#     """
#     Get a transaction given a transaction_id.
#     """
#     return crud.get_transaction_by_id(db, transaction_id)

# @app.patch("/update_transaction/{transaction_id}", response_model=transaction)
# def patch_transaction(transaction_id: int, db: Session = Depends(get_db)):
#     """
#     Update a transaction in the table.
#     """
#     return update_transaction(db, new_transaction)
