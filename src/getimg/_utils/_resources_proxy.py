from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `getimg.resources` module.

    This is used so that we can lazily import `getimg.resources` only when
    needed *and* so that users can just import `getimg` and reference `getimg.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("getimg.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
