import time

from UseFul import NThread
from threading import active_count

i = 0


def fprint():
    global i
    print(i, flush=True)
    i += 1


if __name__ == '__main__':
    print('num thr', active_count())
    tt = NThread(0.5, fprint, ())
    tt.run()
    print('num thr', active_count())
    time.sleep(5)
    tt.stop()
    print('i', i)
    print('num thr', active_count())
    time.sleep(1)
    tt.start()
    time.sleep(10)
    tt.stop()
    print('i', i)
