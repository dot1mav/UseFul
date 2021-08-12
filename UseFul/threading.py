__all__ = ["StoppableThread", "_Thread", "TimerThread", "thread_function"]

from dataclasses import dataclass
from threading import Thread, Timer, Event, ThreadError
from typing import Callable, Optional, Any, Union


class StoppableThread(Thread):
    """
    class to make thread with event
    """

    def __init__(self, *args, **kwargs) -> None:
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.__stop: bool = False

    def start(self) -> None:
        """
        start the thread with Thread().start()
        """
        if not self.__stop:
            super(StoppableThread, self).start()

    def run(self) -> None:
        """
        start thread with Thread().run()
        """
        if not self.__stop:
            super(StoppableThread, self).run()

    def stop(self) -> None:
        """
        set stop event
        """
        self.__stop = True

    def is_stop(self) -> bool:
        """
        check thread is stopped
        :return bool:
        """
        return self.__stop


class Thread_(StoppableThread):
    def __init__(self, target: Optional[Callable[..., Any]], event: Optional[Union[Event, None]] = None, *args, **kwargs) -> None:
        super(Thread_, self).__init__(target=target, *args, **kwargs)
        self._event = event if event else Event()

    @property
    def event(self) -> Event:
        """
        get event
        """
        return self._event

    @event.setter
    def event(self, event: Event) -> None:
        """
        set event
        """
        self._event = event

    @event.deleter
    def event(self):
        """
        set event to none
        """
        self._event = None


class TimerThread:
    """
    for run function in period of time with thread
    """

    def __init__(self, period: float, target: Callable, args: tuple = tuple()):
        self.stopped: bool = False
        self.args: tuple = args
        self.method: Callable = target
        self.period: float = period
        self.task: Timer = None

    def _schedule(self):
        self.stopped = False
        self.task = Timer(self.period, function=self.run, args=self.args)
        self.task.start()

    def run(self):
        """
        make timer object and run timer in period time
        """
        self.method(*self.args)
        self._schedule()

    def stop(self):
        """
        change status stop and cancel timer obj
        """
        self.stopped = True
        if self.task:
            self.task.cancel()
            self.task.join()

    def start(self):
        self.run()

@dataclass
class __ThreadFunction:
    _func: Callable
    __name: str

    def start(self, *args):
        """
        start the thread with argument to pass function
        ** if thread exist raise **
        """
        if "thread" not in self.__dict__.keys():
            self._args: list[Any] = [*args]
            self.__dict__["thread"] = Thread_(
                target=self._func, name=self.__name, args=self._args)
            self.__dict__["thread"].start()
        else:
            raise ThreadError(f"thread has been started {self.__dict__['thread']}")

    def stop(self):
        """
        stop thread and make object null
        ** if not thread exist raise **
        """
        if "thread" in self.__dict__.keys():
            self.__dict__["thread"].stop()
            del self.__dict__["thread"]
        else:
            raise ThreadError("thread not start yet!!!")

    def is_stop(self):
        """
        check thread exist or not
        """
        return False if "thread" in self.__dict__.keys() else True

def thread_function(func: Callable) -> __ThreadFunction:
    return __ThreadFunction(func, func.__name__)
