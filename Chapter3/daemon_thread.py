import threading
import time


def standard_thread():
    print("Starting my standard thread")
    time.sleep(20)
    print("Ending my standard thread")


def daemon_thread():
    while True:
        print("Sending out heartbeat signal")
        time.sleep(2)


if __name__ == '__main__':
    standard_thread_obj = threading.Thread(target=standard_thread)
    daemon_thread_obj = threading.Thread(target=daemon_thread, daemon=True)

    daemon_thread_obj.start()
    standard_thread_obj.start()
