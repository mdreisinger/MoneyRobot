"""
SQLAlchemy models.
"""
# pylint: disable=no-name-in-module

from sqlalchemy import text, Column, Integer, String, Date, Float, TIMESTAMP

from .database import Base


# pylint:disable=too-few-public-methods
class transactions(Base):
    """
    The transactions table model.
    """
    __tablename__ = "transactions"

    transaction_id = Column(Integer, primary_key=True)
    transaction_date = Column(Date, server_default=text("(CURRENT_DATE)"))
    transactor = Column(String)
    transaction_category = Column(String)
    items = Column(String)
    transaction_amount = Column(Float)
    time_modified = Column(TIMESTAMP, 
                           server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
