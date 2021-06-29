__all__ = ['StoppableThread', '_Thread', 'TimerThread', 'thread_function']

from threading import Thread, Timer, Event, Lock, RLock
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

        """
        if not self.__stop:
            print("start")
            super(StoppableThread, self).start()

    def run(self) -> None:
        """
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


class _Thread(StoppableThread):
    def __init__(self, target: Optional[Callable[..., Any]], event: Optional[Union[Event, None]] = None,
                 lock: Optional[Union[Lock, RLock, None]] = None, *args, **kwargs) -> None:
        super(_Thread, self).__init__(target=target, *args, **kwargs)
        self._event = event if event else Event()
        self._lock = lock

    @property
    def event(self) -> Event:
        return self._event

    @event.setter
    def event(self, event: Event) -> None:
        self._event = event

    @property
    def lock(self) -> Lock:
        return self._lock

    @lock.setter
    def lock(self, lock: Union[Lock, RLock]) -> None:
        self._lock = lock


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


def thread_function(func: Callable):
    print(func)
    return _Thread(target=func, name=func.__name__)
