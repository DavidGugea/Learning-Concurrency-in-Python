import threading
import time

def my_thread():
    print(f"Thread {threading.current_thread().name} starting")
    time.sleep(5)
    print(f"Thread {threading.current_thread().name} ending")


for i in range(4):
    thread_name = f"Thread-{i}"
    thread = threading.Thread(name=thread_name, target=my_thread)
    thread.start()


print(f"{threading.enumerate()}")
