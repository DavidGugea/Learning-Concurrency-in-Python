import threading
import time
import random


def my_thread(i):
    print(f"Thread {i}: started")
    time.sleep(random.randint(1, 5))
    print(f"Thread {i}: finished")


def main():
    for i in range(random.randint(2, 50)):
        thread = threading.Thread(target=my_thread, args=(i,))
        thread.start()

    time.sleep(4)
    print("Total number of active thread: {0}".format(
        threading.active_count()
    ))


if __name__ == '__main__':
    main()
