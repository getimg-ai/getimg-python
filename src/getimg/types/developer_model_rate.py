# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeveloperModelRate"]


class DeveloperModelRate(BaseModel):
    billable_unit: str
    """Unit billed, such as image or video_second."""

    resolution: Optional[str] = None
    """Resolution this rate applies to, or null for a resolution-independent rate."""

    sound: Literal["sound_on", "sound_off", "not_applicable"]
    """
    Sound setting this rate applies to; not_applicable also serves as a video
    fallback.
    """

    unit_price: str
    """USD price per billable unit, represented as a decimal string."""
