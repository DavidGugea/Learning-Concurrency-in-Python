import threading
import time


# A very simple method for our thread to execute
def thread_worker():
    # it is only at the point where the thread starts executing that it's state goes from 'Runnable' to a 'Running'
    # state
    print("My Thread has entered the 'Running' State")
    # If we call the time.sleep() method then our thread goes into a not-runnable state. We can do no further work on
    # this particular thread
    print('before sleep')
    time.sleep(2)
    print('after sleep')
    # Thread then completes its tasks and terminates
    print("My Thread is terminating")


# At this point in time, the thread has no state it hasn't been allocated any system resources
my_thread = threading.Thread(target=thread_worker)

# When we call my_thread.start(), Python allocates the necessary system resources in order for our thread to run and
# then calls the thread's run method. It goes from 'starting' state to 'Runnable' but not running
my_thread.start()

# Here we join the thread and when this method is called our thread goes into a 'Dead' state. It has finished the job
# that it was intended to do.
print('test 1')
my_thread.join()
print('test 2')

print("My Thread has entered a 'Dead' state")
