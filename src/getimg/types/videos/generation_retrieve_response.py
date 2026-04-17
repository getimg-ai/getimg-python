# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..usage import Usage
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "GenerationRetrieveResponse",
    "VideoGenerationPendingResponse",
    "VideoGenerationFailedResponse",
    "VideoGenerationFailedResponseError",
    "VideoGenerationCompletedResponse",
    "VideoGenerationCompletedResponseData",
]


class VideoGenerationPendingResponse(BaseModel):
    id: str
    """The ID of the generation request."""

    status: Literal["pending"]
    """The status of the generation request."""


class VideoGenerationFailedResponseError(BaseModel):
    code: str
    """The error code."""

    message: str
    """The error message."""


class VideoGenerationFailedResponse(BaseModel):
    id: str
    """The ID of the generation request."""

    error: VideoGenerationFailedResponseError

    status: Literal["failed"]
    """The status of the generation request."""


class VideoGenerationCompletedResponseData(BaseModel):
    deletes_at: datetime
    """The date and time the video will be deleted."""

    mime_type: str
    """The MIME type of the video."""

    url: str
    """Signed temporary download URL."""

    duration: Optional[float] = None
    """The duration of the video in seconds."""

    fps: Optional[float] = None
    """The frame rate of the video."""

    has_sound: Optional[bool] = None
    """Whether the video has and audio track."""

    height: Optional[int] = None
    """The height of the video in pixels."""

    width: Optional[int] = None
    """The width of the video in pixels."""


class VideoGenerationCompletedResponse(BaseModel):
    id: str
    """The ID of the generation request."""

    data: List[VideoGenerationCompletedResponseData]
    """The media items for the generation."""

    model: str
    """The model used for the generation."""

    status: Literal["completed"]
    """The status of the generation request."""

    usage: Optional[Usage] = None


GenerationRetrieveResponse: TypeAlias = Annotated[
    Union[VideoGenerationPendingResponse, VideoGenerationFailedResponse, VideoGenerationCompletedResponse],
    PropertyInfo(discriminator="status"),
]
