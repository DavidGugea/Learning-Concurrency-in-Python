from multiprocessing import Process
import time


def my_worker():
    print(f"Process started at: {time.ctime(time.time())}")
    time.sleep(20)


my_process = Process(target=my_worker)
print(f"Process: {my_process}")
my_process.start()
print("Terminating Process...")
my_process.terminate()
my_process.join()
print(f"Process terminated: {my_process}")
