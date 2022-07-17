import threading
import time


def task(seconds: int) -> None:
    print(f'Waiting for {seconds} second(s)')

    time.sleep(seconds)

    print(f'Finished waiting for {seconds} second(s)')


start_time = time.perf_counter()

thread_1 = threading.Thread(target=task, args=(1, ))
thread_2 = threading.Thread(target=task, args=(1, ))

thread_1.run()
thread_2.run()

thread_1.join()
thread_2.join()

end_time = time.perf_counter()

print(f'Finished executing the program. Time needed: {round(end_time - start_time, 2)} second(s)')