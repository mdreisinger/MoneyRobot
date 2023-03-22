"""
crud.py
"""

from sqlalchemy import Date
from sqlalchemy.orm import Session

from .models import transactions
from .schemas import transaction


def add_transaction(db: Session, new_transaction: transaction):
    """
    Function to add a transaction to the database.
    """
    if not new_transaction.tax_included:
        new_transaction.transaction_amount = new_transaction.transaction_amount +\
                         new_transaction.transaction_amount * (new_transaction.tax_rate/100)
    db_transaction = transactions(transactor=new_transaction.transactor,
                                  transaction_category=new_transaction.transaction_category,
                                  items=new_transaction.items,
                                  transaction_amount=new_transaction.transaction_amount)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

def get_transaction_by_id(db: Session, transaction_id: int):
    """
    Get a transaction given a transaction_id.
    """
    return db.query(transactions).filter(transactions.transaction_id == transaction_id)

# def get_transactions_by_date(db: Session, transaction_date: Date):
#     """
#     Get transactions given a date.
#     """
#     return db.query(transactions).filter(transactions.transaction_date == transaction_date)

# def get_all_transactions(db: Session):
#     """
#     Get a lot of transactions.
#     """
#     return db.query(transactions).all()

# def update_transaction_amount(db: Session, existing_transaction_id: int, 
#                               new_transaction_amount: transaction.transaction_amount):
#     """
#     Function to modify a transaction to the database.
#     """
#     transaction_to_update = get_transaction_by_id(db, existing_transaction_id)
#     transaction_to_update.transaction_amount = new_transaction_amount
#     db.commit()
#     db.refresh(transaction_to_update)
#     return transaction_to_update
