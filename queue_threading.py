import queue
import time
import threading

class SampleThread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print(f"Initializing {self.name}")
        while True:
            try:
                data = self.q.get(timeout=2)  # Timeout to prevent hanging
                print(f"{self.name} processing {data}")
                time.sleep(1)  # Simulate processing time
                self.q.task_done()  # Mark the task as done
            except queue.Empty:
                break  # Exit loop when queue is empty
        print(f"Exiting {self.name}")

# Initialize thread names and queue
thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["A", "B", "C", "D", "E"]
workQueue = queue.Queue()

threads = []
threadID = 1

# Create new threads
for thread_name in thread_list:
    thread = SampleThread(threadID, thread_name, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Fill the queue
for item in name_list:
    workQueue.put(item)

# Wait for all items in the queue to be processed
workQueue.join()

# Wait for all threads to complete
for t in threads:
    t.join()

print("Exit Main Thread")
