# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .developer_model_rate import DeveloperModelRate

__all__ = ["ModelRetrieveResponse", "Pricing"]


class Pricing(BaseModel):
    currency: Literal["USD"]

    rates: List[DeveloperModelRate]
    """Currently effective catalog rates, ordered by unit price.

    Empty when no active rates are configured; this does not mean generation is
    free.
    """


class ModelRetrieveResponse(BaseModel):
    id: str
    """The model identifier."""

    created_at: datetime
    """Timestamp when the model was created."""

    name: str
    """The model display name."""

    pricing: Pricing

    supported_aspect_ratios: List[str]
    """Supported aspect ratios in default order; the first is used when omitted."""

    supported_durations: List[float]
    """Supported durations in seconds; empty for image models.

    The first is the default.
    """

    supported_references: Dict[str, int]
    """
    Maximum reference count per supported role (reference_image, first_frame,
    last_frame).
    """

    supported_resolutions: List[str]
    """Supported resolutions in default order; the first is used when omitted."""

    supports_sound: bool
    """Whether sound generation is supported."""

    type: Literal["image", "video"]
    """The generation type supported by the model."""
