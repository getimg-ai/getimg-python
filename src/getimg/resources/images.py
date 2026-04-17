# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import image_generate_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.image_generate_response import ImageGenerateResponse

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    """Endpoints for image generation."""

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/getimg-ai/getimg-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/getimg-ai/getimg-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def generate(
        self,
        *,
        model: str,
        prompt: str,
        aspect_ratio: str | Omit = omit,
        images: Iterable[image_generate_params.Image] | Omit = omit,
        output_format: Literal["png", "jpeg", "webp"] | Omit = omit,
        resolution: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse:
        """Generate an image and return the completed result.

        Args:
          model: AI model ID.

        See [supported models](https://getimg.ai/app/developer/models).

          prompt: Description of the image to generate or an editing instruction.

          aspect_ratio: Optional output aspect ratio. See
              [supported values by model](https://getimg.ai/app/developer/models).

          output_format: Output image format.

          resolution: Optional output resolution. See
              [supported values by model](https://getimg.ai/app/developer/models).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/images/generations",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "aspect_ratio": aspect_ratio,
                    "images": images,
                    "output_format": output_format,
                    "resolution": resolution,
                },
                image_generate_params.ImageGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerateResponse,
        )


class AsyncImagesResource(AsyncAPIResource):
    """Endpoints for image generation."""

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/getimg-ai/getimg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/getimg-ai/getimg-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def generate(
        self,
        *,
        model: str,
        prompt: str,
        aspect_ratio: str | Omit = omit,
        images: Iterable[image_generate_params.Image] | Omit = omit,
        output_format: Literal["png", "jpeg", "webp"] | Omit = omit,
        resolution: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageGenerateResponse:
        """Generate an image and return the completed result.

        Args:
          model: AI model ID.

        See [supported models](https://getimg.ai/app/developer/models).

          prompt: Description of the image to generate or an editing instruction.

          aspect_ratio: Optional output aspect ratio. See
              [supported values by model](https://getimg.ai/app/developer/models).

          output_format: Output image format.

          resolution: Optional output resolution. See
              [supported values by model](https://getimg.ai/app/developer/models).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/images/generations",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "aspect_ratio": aspect_ratio,
                    "images": images,
                    "output_format": output_format,
                    "resolution": resolution,
                },
                image_generate_params.ImageGenerateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ImageGenerateResponse,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.generate = to_raw_response_wrapper(
            images.generate,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.generate = async_to_raw_response_wrapper(
            images.generate,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.generate = to_streamed_response_wrapper(
            images.generate,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.generate = async_to_streamed_response_wrapper(
            images.generate,
        )
