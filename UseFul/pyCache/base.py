__all__ = ['CacheBase']

from abc import ABC, abstractclassmethod


class CacheBase(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    async def _connect(self) -> None:
        await ...
