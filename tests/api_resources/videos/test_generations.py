# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from getimg import GetimgAI, AsyncGetimgAI
from tests.utils import assert_matches_type
from getimg.types.videos import GenerationCreateResponse, GenerationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: GetimgAI) -> None:
        generation = client.videos.generations.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: GetimgAI) -> None:
        generation = client.videos.generations.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
            aspect_ratio="16:9",
            duration=5,
            images=[
                {
                    "role": "reference_image",
                    "url": "x",
                }
            ],
            resolution="1080p",
            sound=False,
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: GetimgAI) -> None:
        response = client.videos.generations.with_raw_response.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: GetimgAI) -> None:
        with client.videos.generations.with_streaming_response.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: GetimgAI) -> None:
        generation = client.videos.generations.retrieve(
            "x",
        )
        assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: GetimgAI) -> None:
        response = client.videos.generations.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = response.parse()
        assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: GetimgAI) -> None:
        with client.videos.generations.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = response.parse()
            assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: GetimgAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.videos.generations.with_raw_response.retrieve(
                "",
            )


class TestAsyncGenerations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGetimgAI) -> None:
        generation = await async_client.videos.generations.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGetimgAI) -> None:
        generation = await async_client.videos.generations.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
            aspect_ratio="16:9",
            duration=5,
            images=[
                {
                    "role": "reference_image",
                    "url": "x",
                }
            ],
            resolution="1080p",
            sound=False,
        )
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGetimgAI) -> None:
        response = await async_client.videos.generations.with_raw_response.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationCreateResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGetimgAI) -> None:
        async with async_client.videos.generations.with_streaming_response.create(
            model="seedance-v1-pro",
            prompt="A drone shot over a futuristic city skyline at sunset",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationCreateResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGetimgAI) -> None:
        generation = await async_client.videos.generations.retrieve(
            "x",
        )
        assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGetimgAI) -> None:
        response = await async_client.videos.generations.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generation = await response.parse()
        assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGetimgAI) -> None:
        async with async_client.videos.generations.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generation = await response.parse()
            assert_matches_type(GenerationRetrieveResponse, generation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncGetimgAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.videos.generations.with_raw_response.retrieve(
                "",
            )
