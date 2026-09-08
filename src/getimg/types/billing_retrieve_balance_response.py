# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BillingRetrieveBalanceResponse"]


class BillingRetrieveBalanceResponse(BaseModel):
    balance: str
    """Current balance in USD."""

    currency: Literal["USD"]
