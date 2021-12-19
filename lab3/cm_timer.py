import time
from contextlib import contextmanager
from time import sleep


@contextmanager
def cm_timer_2():
    try:
        begin = time.perf_counter()
        yield begin
    finally:
        print(time.perf_counter() - begin)


class cm_timer_1():

    def start(self):
        self.begin = time.perf_counter()

    def stop(self):
        work = time.perf_counter() - self.begin
        print(work)

    def __enter__(self):
        self.start()

    def __init__(self):
        self.startTime = time.time()

    def __exit__(self, *args):
        self.stop()


with cm_timer_1():
    sleep(5.5)


with cm_timer_2():
    sleep(5.5)

