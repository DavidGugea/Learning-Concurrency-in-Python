import threading
import concurrent.futures
import time
from typing import List

start = time.perf_counter()


def do_something(seconds: int) -> str:
    print(f'Sleeping {seconds} second(s)...')

    time.sleep(seconds)

    return f'Done sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = list(range(1, 6))[::-1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

"""
threads: List[threading.Thread] = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
"""

# using 'join' means that the threads will get to complete before continuing calculating the finish time

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} seconds(s)')
