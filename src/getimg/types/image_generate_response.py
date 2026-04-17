# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .usage import Usage
from .._models import BaseModel

__all__ = ["ImageGenerateResponse", "Data"]


class Data(BaseModel):
    deletes_at: datetime
    """The date and time the image will be deleted."""

    mime_type: str
    """The MIME type of the image."""

    url: str
    """Signed temporary download URL."""

    height: Optional[int] = None
    """The height of the image in pixels."""

    width: Optional[int] = None
    """The width of the image in pixels."""


class ImageGenerateResponse(BaseModel):
    id: str
    """The ID of the generation request."""

    data: List[Data]
    """The media items for the generation."""

    model: str
    """The model used for the generation."""

    status: Literal["completed"]

    usage: Usage
