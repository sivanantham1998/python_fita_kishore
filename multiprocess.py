import multiprocessing
import time

def a():
    time.sleep(3)
    print("a function started.....")

def b():
    time.sleep(3)
    print("b function started.....")

if __name__=="__main__":
    start=time.time()
    a()
    b()
    end=time.time()
    print("Normal time taken",end-start)

    # multiprocess
    start=time.time()
    p1=multiprocessing.Process(target=a)
    p2=multiprocessing.Process(target=b)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end=time.time()
    print("Multiprocess time taken",end-start)