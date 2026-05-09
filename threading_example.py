import threading
import time

def a():
    time.sleep(3)
    print("a function started...")

def b():
    time.sleep(3)
    print("b function started...")

if __name__=="__main__":
    start=time.time()
    a()
    b()
    end=time.time()
    print("Normal time taken",end-start)

    # multithreading
    start=time.time()
    t1=threading.Thread(target=a)
    t2=threading.Thread(target=b)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end=time.time()
    print("Multithreading time taken",end-start)



from concurrent.futures import ThreadPoolExecutor
import time

def task(name):
    print(f"Starting task {name}")
    time.sleep(1)  # Simulate I/O work
    return f"Task {name} completed"

# Create a pool with 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # submit() returns a Future object immediately
    future1 = executor.submit(task, "A")
    future2 = executor.submit(task, "B")
    
    # Retrieve results (this blocks until the task is done)
    print(future1.result())
    print(future2.result())
