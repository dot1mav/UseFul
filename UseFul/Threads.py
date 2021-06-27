from threading import Thread, Timer
from typing import Optional


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
    def __init__(self, period, method, args):
        self.stopped = False
        self.args = args
        self.method = method
        self.period = period
        self.task = None

    def schedule(self):
        if not self.stopped:
            self.task = Timer(self.period, self.run, [])
            self.task.start()

    def run(self):
        if not self.stopped:
            self.method(*self.args)
            self.schedule()

    def stop(self):
        self.stopped = True
        if self.task:
            self.task.cancel()
            self.task.join()

    def start(self):
        self.schedule()
