__all__ = ['create_cache']
__doc__ = ''''''

from typing import Union
from .base import CacheBase
from .Cache import FileCache, RedisCache


def create_cache(mode: str = 'redis') -> Union[RedisCache, FileCache, CacheBase]:
    if mode.upper() == 'REDIS':
        return RedisCache()
    elif mode.upper() == 'FILESYSTEM':
        return FileCache()
    else:
        raise Exception('!!!Mode not supported yet!!!')
