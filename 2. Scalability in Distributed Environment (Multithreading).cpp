import threading
import queue
import time

tasks = queue.Queue()

for i in range(5):
    tasks.put(f"Task {i}")

def worker(id):
    while not tasks.empty():
        try:
            t = tasks.get_nowait()
        except:
            break
        print(f"Worker {id} processing {t}")
        time.sleep(0.5)
        print(f"Worker {id} finished {t}")
        tasks.task_done()

threads = []

for i in range(2):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All tasks completed.")



  
