import threading
import time
import random
import pprint


def my_thread(i):
    print(f"Thread {i}: started")

    time.sleep(random.randint(1, 5))

    print(f"Thread {i}: ended")


def main():
    for i in range(4):
        thread = threading.Thread(target=my_thread, args=(i,))
        thread.start()

    print(f"Enumerating: \n{pprint.pformat(threading.enumerate(), indent=10)}")


if __name__ == '__main__':
    main()
