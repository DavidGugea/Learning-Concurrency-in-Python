import threading
import urllib.request
import time


def download_image(image_path: str, file_name: str) -> None:
    print("Downloading Image from ", image_path)
    urllib.request.urlretrieve(image_path, file_name)
    print("Completed Download")


def execute_thread(i):
    image_name = "temp/image-" + str(i) + ".jpg"
    download_image("http://lorempixel.com/400/200/sports", image_name)


def main():
    t0 = time.time()

    # create an array which will store a reference to all of our threads
    threads = []

    # create 10 threads, append them to our array of threadsa and start them off
    for i in range(10):
        thread = threading.Thread(target=execute_thread, args=(i,))
        threads.append(thread)
        thread.start()

    # ensure that all the threads in our array have completed their execution before we log the total time to complete
    for i in threads:
        i.join()

    # calculate the total execution time
    t1 = time.time()
    total_time = t1 - t0
    print("Total Execution Time {0}".format(total_time))


if __name__ == '__main__':
    main()
