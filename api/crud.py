"""
crud.py
"""

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
