import threading
import time
import random


def execute_thread(i):
    print(f"Thread {i} started")
    sleep_time = random.randint(1, 10)
    time.sleep(sleep_time)
    print(f"Thread {i} finished executing")


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i, ))
    thread.start()
    print("Active threads: {0}".format(threading.enumerate()))