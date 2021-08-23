from UseFul import Thread_
from threading import current_thread
from time import sleep

i: int = 0
j: int = 0


def counter_j():
    global j
    thread: Thread_ = current_thread()
    print(f'start {counter_j=}')
    while not thread.is_stop():
        j += 1
        if j == 5:
            thread.event.wait()
        sleep(0.1)
    j = 0
    print(f'stop {counter_j=}')


def counter_i():
    global i
    thread: Thread_ = current_thread()
    print(f'start {counter_i=}')
    while not thread.is_stop():
        i += 1
        if i % 5 == 0:
            thread.event.wait()
        sleep(0.1)
    print(f'stop {counter_i=}')


thread_i = Thread_(target=counter_i, name=counter_i.__name__)
thread_j = Thread_(target=counter_j, name=counter_j.__name__)


print(f'{i=} / {j=}')
thread_i.start()
sleep(0.8)
print(f'{i=} / {j=}')
thread_j.start()
sleep(0.8)
print(f'{i=} / {j=}')
thread_i.event.set()
sleep(0.4)
print(f'{i=} / {j=}')
thread_j.event.set()
sleep(0.4)
print(f'{i=} / {j=}')
thread_i.stop()
thread_j.stop()
sleep(0.2)
print(f'{i=} / {j=}')
