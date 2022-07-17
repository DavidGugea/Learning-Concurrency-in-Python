import threading
from multiprocessing import Process
import time


def my_task():
    print("Starting")
    time.sleep(2)


t0 = time.perf_counter()
threads = []

for _ in range(10):
    thread = threading.Thread(target=my_task)
    thread.start()
    threads.append(thread)

t1 = time.perf_counter()
print(f"Total time for creating 10 threads: {round(t1 - t0, 2)} seconds")

for thread in threads:
    thread.join()

t2 = time.perf_counter()
procs = []

for _ in range(10):
    process = Process(target=my_task)
    process.start()
    procs.append(process)

t3 = time.perf_counter()

print(f"Total time for creating 10 processes: {round(t3 - t2, 2)} seconds")

for proc in procs:
    proc.join()