import threading
import time


def my_child_thread():
    print("Child thread starting")
    time.sleep(5)
    print("Current thread ----------")
    print(threading.current_thread())
    print("-------------------------")
    print("Main thread -------------")
    print(threading.main_thread())
    print("-------------------------")
    print("Child thread ending")


child = threading.Thread(target=my_child_thread)
child.start()
child.join()
