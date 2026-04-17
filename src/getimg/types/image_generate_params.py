# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImageGenerateParams", "Image"]


class ImageGenerateParams(TypedDict, total=False):
    model: Required[str]
    """AI model ID. See [supported models](https://getimg.ai/app/developer/models)."""

    prompt: Required[str]
    """Description of the image to generate or an editing instruction."""

    aspect_ratio: str
    """Optional output aspect ratio.

    See [supported values by model](https://getimg.ai/app/developer/models).
    """

    images: Iterable[Image]

    output_format: Literal["png", "jpeg", "webp"]
    """Output image format."""

    resolution: str
    """
    Optional output resolution. See
    [supported values by model](https://getimg.ai/app/developer/models).
    """


class Image(TypedDict, total=False):
    url: Required[str]
    """Publicly accessible reference image URL."""
