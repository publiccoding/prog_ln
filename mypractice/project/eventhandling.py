import threading
import time
import numpy as np 


def eventstart():
    time.sleep(3)
    event.set()
    print("Event is set")
    if not event.is_set():
        exit(0)
    time.sleep(7)
    print("event will be cleared")
    print(event.is_set())
 

def eventstop(num):
    print("event is waiting")
    event.wait()
    while event.is_set():
        x= np.random.randint(1,num)
        time.sleep(0.1)
        print(x)
        if x == 29:
            print("Event will be cleare and the value is ",x)
            event.clear()
            exit(0)
    
if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=eventstart)
    t2 = threading.Thread(target=eventstop,args=(30,))
    t1.start()
    t2.start()
    