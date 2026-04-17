# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ModelListResponse", "ModelListResponseItem"]


class ModelListResponseItem(BaseModel):
    id: str
    """The model identifier."""

    created_at: datetime
    """Timestamp when the model was created."""

    name: str
    """The model display name."""

    type: Literal["image", "video"]
    """The generation type supported by the model."""


ModelListResponse: TypeAlias = List[ModelListResponseItem]
