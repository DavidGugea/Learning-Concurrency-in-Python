import threading
import time
import random

counter = 1


def worker_a():
    global counter
    while counter < 1000:
        counter += 1
        print("Worker A is incrementing counter to {0}".format(counter))
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)


def worker_b():
    global counter
    while counter > -1000:
        counter -= 1
        print("Worker B is decrementing counter to {0}".format(counter))
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)


def main():
    t0 = time.perf_counter()

    thread1 = threading.Thread(target=worker_a)
    thread2 = threading.Thread(target=worker_b)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.perf_counter()

    print("Execution time {0}".format(t1 - t0))


if __name__ == '__main__':
    main()
