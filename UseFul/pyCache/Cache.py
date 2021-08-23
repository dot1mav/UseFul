__all__ = ['FileCache']

from .base import CacheBase


class FileCache(CacheBase):
    def __init__(self) -> None:
        super().__init__()

    def _connect(self) -> None:
        return super()._connect()


class RedisCache(CacheBase):
    def __init__(self) -> None:
        super().__init__()

    def _connect(self) -> None:
        return super()._connect()
