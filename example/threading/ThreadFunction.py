from UseFul import thread_function
from time import sleep


@thread_function
def counter(i):
    while not counter.is_stop():
        print(f"{counter=}\t{i=}")
        i+=1
        sleep(0.1)


if __name__ == "__main__":
    #first we need start the thread
    counter.start(0) # start with argument or arguments
    sleep(.6) # now we should wait to see outputs
    counter.stop() # now stop thread
    # and we can do it again like this

    sleep(.4)
    counter.start(-100)
    sleep(.3)
    counter.stop()