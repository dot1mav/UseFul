__all__ = ["func_log"]
__doc__ = """"""

from . import FLOGGER
from functools import wraps
from typing import Callable


def func_log(func: Callable):
    """Logging for your functions when they start and stop or end 
you need to create a handler
in functions you get log attr for sending more logs
and flag attr to show that function have been stopped or ended
    """
    @wraps(func)
    def wraps_(*args, **kwargs):
        FLOGGER.info(f"{func.__name__}_start")
        wraps_.flag = False
        wraps_.log = FLOGGER
        value = func(*args, **kwargs)
        if wraps_.flag:
            FLOGGER.warning(f"{func.__name__}_stop")
        else:
            FLOGGER.info(f"{func.__name__}_end")
        return value
    return wraps_
