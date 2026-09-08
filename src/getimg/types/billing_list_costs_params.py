# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BillingListCostsParams"]


class BillingListCostsParams(TypedDict, total=False):
    end: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive ISO 8601 end timestamp.

    Must include a time zone, fall after `start`, and sit within 180 days of it.
    """

    start: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Inclusive ISO 8601 start timestamp. Must include a time zone."""
