"""
Models for the API.
"""

import datetime
from typing import Optional

from pydantic import BaseModel

class transaction(BaseModel):
    """
    Class to define the transaction model for the API.
    """
    transaction_date: Optional[datetime.date]
    transactor: str
    transaction_category: str
    items: str
    transaction_amount: float
    tax_included: Optional[bool] = True
    tax_rate: Optional[float] = 8.645

    # pylint:disable=too-few-public-methods
    class Config:
        """
        orm_mode will tell the Pydantic model to read the data even if it is not a dict,
        but an ORM model (or any other arbitrary object with attributes).
        This way, instead of only trying to get the id value from a dict, as in:

        id = data["id"]

        it will also try to get it from an attribute, as in:

        id = data.id
        """
        orm_mode = True
