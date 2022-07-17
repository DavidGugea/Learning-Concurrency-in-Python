import threading


def thread_target():
    print(f"Current thread: {threading.current_thread()}")


threads = []

for _ in range(10):
    thread = threading.Thread(target=thread_target)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
