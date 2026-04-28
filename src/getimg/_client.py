# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import GetimgAIError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import images, models, videos
    from .resources.images import ImagesResource, AsyncImagesResource
    from .resources.models import ModelsResource, AsyncModelsResource
    from .resources.videos.videos import VideosResource, AsyncVideosResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "GetimgAI",
    "AsyncGetimgAI",
    "Client",
    "AsyncClient",
]


class GetimgAI(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous GetimgAI client instance.

        This automatically infers the `api_key` argument from the `GETIMG_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GETIMG_API_KEY")
        if api_key is None:
            raise GetimgAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GETIMG_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GETIMG_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.getimg.ai"

        custom_headers_env = os.environ.get("GETIMG_AI_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def images(self) -> ImagesResource:
        """Endpoints for image generation."""
        from .resources.images import ImagesResource

        return ImagesResource(self)

    @cached_property
    def videos(self) -> VideosResource:
        from .resources.videos import VideosResource

        return VideosResource(self)

    @cached_property
    def models(self) -> ModelsResource:
        """Endpoints for listing available developer models."""
        from .resources.models import ModelsResource

        return ModelsResource(self)

    @cached_property
    def with_raw_response(self) -> GetimgAIWithRawResponse:
        return GetimgAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GetimgAIWithStreamedResponse:
        return GetimgAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGetimgAI(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGetimgAI client instance.

        This automatically infers the `api_key` argument from the `GETIMG_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GETIMG_API_KEY")
        if api_key is None:
            raise GetimgAIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the GETIMG_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GETIMG_AI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.getimg.ai"

        custom_headers_env = os.environ.get("GETIMG_AI_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def images(self) -> AsyncImagesResource:
        """Endpoints for image generation."""
        from .resources.images import AsyncImagesResource

        return AsyncImagesResource(self)

    @cached_property
    def videos(self) -> AsyncVideosResource:
        from .resources.videos import AsyncVideosResource

        return AsyncVideosResource(self)

    @cached_property
    def models(self) -> AsyncModelsResource:
        """Endpoints for listing available developer models."""
        from .resources.models import AsyncModelsResource

        return AsyncModelsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncGetimgAIWithRawResponse:
        return AsyncGetimgAIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGetimgAIWithStreamedResponse:
        return AsyncGetimgAIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._bearer_auth if security.get("bearer_auth", False) else {}),
        }

    @property
    def _bearer_auth(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GetimgAIWithRawResponse:
    _client: GetimgAI

    def __init__(self, client: GetimgAI) -> None:
        self._client = client

    @cached_property
    def images(self) -> images.ImagesResourceWithRawResponse:
        """Endpoints for image generation."""
        from .resources.images import ImagesResourceWithRawResponse

        return ImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def videos(self) -> videos.VideosResourceWithRawResponse:
        from .resources.videos import VideosResourceWithRawResponse

        return VideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def models(self) -> models.ModelsResourceWithRawResponse:
        """Endpoints for listing available developer models."""
        from .resources.models import ModelsResourceWithRawResponse

        return ModelsResourceWithRawResponse(self._client.models)


class AsyncGetimgAIWithRawResponse:
    _client: AsyncGetimgAI

    def __init__(self, client: AsyncGetimgAI) -> None:
        self._client = client

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithRawResponse:
        """Endpoints for image generation."""
        from .resources.images import AsyncImagesResourceWithRawResponse

        return AsyncImagesResourceWithRawResponse(self._client.images)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithRawResponse:
        from .resources.videos import AsyncVideosResourceWithRawResponse

        return AsyncVideosResourceWithRawResponse(self._client.videos)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithRawResponse:
        """Endpoints for listing available developer models."""
        from .resources.models import AsyncModelsResourceWithRawResponse

        return AsyncModelsResourceWithRawResponse(self._client.models)


class GetimgAIWithStreamedResponse:
    _client: GetimgAI

    def __init__(self, client: GetimgAI) -> None:
        self._client = client

    @cached_property
    def images(self) -> images.ImagesResourceWithStreamingResponse:
        """Endpoints for image generation."""
        from .resources.images import ImagesResourceWithStreamingResponse

        return ImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def videos(self) -> videos.VideosResourceWithStreamingResponse:
        from .resources.videos import VideosResourceWithStreamingResponse

        return VideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def models(self) -> models.ModelsResourceWithStreamingResponse:
        """Endpoints for listing available developer models."""
        from .resources.models import ModelsResourceWithStreamingResponse

        return ModelsResourceWithStreamingResponse(self._client.models)


class AsyncGetimgAIWithStreamedResponse:
    _client: AsyncGetimgAI

    def __init__(self, client: AsyncGetimgAI) -> None:
        self._client = client

    @cached_property
    def images(self) -> images.AsyncImagesResourceWithStreamingResponse:
        """Endpoints for image generation."""
        from .resources.images import AsyncImagesResourceWithStreamingResponse

        return AsyncImagesResourceWithStreamingResponse(self._client.images)

    @cached_property
    def videos(self) -> videos.AsyncVideosResourceWithStreamingResponse:
        from .resources.videos import AsyncVideosResourceWithStreamingResponse

        return AsyncVideosResourceWithStreamingResponse(self._client.videos)

    @cached_property
    def models(self) -> models.AsyncModelsResourceWithStreamingResponse:
        """Endpoints for listing available developer models."""
        from .resources.models import AsyncModelsResourceWithStreamingResponse

        return AsyncModelsResourceWithStreamingResponse(self._client.models)


Client = GetimgAI

AsyncClient = AsyncGetimgAI
