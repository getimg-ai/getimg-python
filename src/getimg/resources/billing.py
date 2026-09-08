# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import billing_list_costs_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.billing_list_costs_response import BillingListCostsResponse
from ..types.billing_retrieve_balance_response import BillingRetrieveBalanceResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    """Developer API balance and usage costs."""

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/getimg-ai/getimg-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/getimg-ai/getimg-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def list_costs(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListCostsResponse:
        """
        Retrieve daily API costs and the range total for your developer project.

        Args:
          end: Inclusive ISO 8601 end timestamp. Must include a time zone, fall after `start`,
              and sit within 180 days of it.

          start: Inclusive ISO 8601 start timestamp. Must include a time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/billing/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    billing_list_costs_params.BillingListCostsParams,
                ),
            ),
            cast_to=BillingListCostsResponse,
        )

    def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBalanceResponse:
        """Retrieve the current API balance shared by the API key's workspace."""
        return self._get(
            "/v2/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveBalanceResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    """Developer API balance and usage costs."""

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/getimg-ai/getimg-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/getimg-ai/getimg-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def list_costs(
        self,
        *,
        end: Union[str, datetime],
        start: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingListCostsResponse:
        """
        Retrieve daily API costs and the range total for your developer project.

        Args:
          end: Inclusive ISO 8601 end timestamp. Must include a time zone, fall after `start`,
              and sit within 180 days of it.

          start: Inclusive ISO 8601 start timestamp. Must include a time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/billing/costs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end": end,
                        "start": start,
                    },
                    billing_list_costs_params.BillingListCostsParams,
                ),
            ),
            cast_to=BillingListCostsResponse,
        )

    async def retrieve_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingRetrieveBalanceResponse:
        """Retrieve the current API balance shared by the API key's workspace."""
        return await self._get(
            "/v2/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingRetrieveBalanceResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_costs = to_raw_response_wrapper(
            billing.list_costs,
        )
        self.retrieve_balance = to_raw_response_wrapper(
            billing.retrieve_balance,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_costs = async_to_raw_response_wrapper(
            billing.list_costs,
        )
        self.retrieve_balance = async_to_raw_response_wrapper(
            billing.retrieve_balance,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.list_costs = to_streamed_response_wrapper(
            billing.list_costs,
        )
        self.retrieve_balance = to_streamed_response_wrapper(
            billing.retrieve_balance,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.list_costs = async_to_streamed_response_wrapper(
            billing.list_costs,
        )
        self.retrieve_balance = async_to_streamed_response_wrapper(
            billing.retrieve_balance,
        )
