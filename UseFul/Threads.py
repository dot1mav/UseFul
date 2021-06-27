__all__ = ['StoppableThread', 'TimerThread']


from threading import Thread, Timer
from typing import Callable, Optional


class StoppableThread(Thread):
    """
    class to make thread with event
    """

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self.__stop: bool = False

    def start(self) -> None:
        self.__stop = False
        super(StoppableThread, self).start()

    def run(self) -> None:
        self.__stop = False
        super(StoppableThread, self).run()

    def join(self, timeout: Optional[float] = ...) -> None:
        super(StoppableThread, self).join(timeout=timeout)

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
