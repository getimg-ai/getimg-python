# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Usage"]


class Usage(BaseModel):
    billable_unit: str
    """The unit of the cost."""

    quantity: float
    """The quantity of the generation."""

    total_cost: float
    """Total cost of the generation."""

    unit_price: float
    """The price of the unit."""
