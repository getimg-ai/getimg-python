# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GenerationCreateResponse"]


class GenerationCreateResponse(BaseModel):
    id: str
    """The ID of the generation request."""

    status: Literal["pending"]
    """The status of the generation request."""
