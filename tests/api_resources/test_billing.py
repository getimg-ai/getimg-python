# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from getimg import GetimgAI, AsyncGetimgAI
from tests.utils import assert_matches_type
from getimg.types import BillingListCostsResponse, BillingRetrieveBalanceResponse
from getimg._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_costs(self, client: GetimgAI) -> None:
        billing = client.billing.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BillingListCostsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_costs(self, client: GetimgAI) -> None:
        response = client.billing.with_raw_response.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingListCostsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_costs(self, client: GetimgAI) -> None:
        with client.billing.with_streaming_response.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingListCostsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_balance(self, client: GetimgAI) -> None:
        billing = client.billing.retrieve_balance()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balance(self, client: GetimgAI) -> None:
        response = client.billing.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: GetimgAI) -> None:
        with client.billing.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_costs(self, async_client: AsyncGetimgAI) -> None:
        billing = await async_client.billing.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BillingListCostsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_costs(self, async_client: AsyncGetimgAI) -> None:
        response = await async_client.billing.with_raw_response.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingListCostsResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_costs(self, async_client: AsyncGetimgAI) -> None:
        async with async_client.billing.with_streaming_response.list_costs(
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingListCostsResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncGetimgAI) -> None:
        billing = await async_client.billing.retrieve_balance()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncGetimgAI) -> None:
        response = await async_client.billing.with_raw_response.retrieve_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncGetimgAI) -> None:
        async with async_client.billing.with_streaming_response.retrieve_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingRetrieveBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True
