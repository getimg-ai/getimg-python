# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingListCostsResponse", "Data"]


class Data(BaseModel):
    cost: float
    """Cost for the bucket in USD."""

    date: datetime.date
    """UTC calendar date for the bucket."""


class BillingListCostsResponse(BaseModel):
    currency: Literal["USD"]

    data: List[Data]
    """One bucket per UTC calendar date in the range."""

    end: datetime.datetime
    """End of the requested range."""

    start: datetime.datetime
    """Start of the requested range."""

    total_cost: float
    """Total cost for the range in USD."""
