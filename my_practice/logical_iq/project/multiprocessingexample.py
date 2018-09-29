from multiprocessing import Pool, Process,Pipe, queues
from random import random 
from math import pi, sqrt
import time 
import os

def  compute_pi(n):
    i, index = 0, 0
    while i < n:
        #time.sleep(0.001)
        x = random()
        y = random()
        if sqrt(x*x + y*y) <= 1:
            index +=1
        i +=1
    ratio = 4.0 * index / n 
    print(ratio)

# if __name__ == '__main__' :
#     mproc1 = Process(target=compute_pi, args=(100000,))
#     mproc1.start()
#     mproc1.join()
#     print("first process completed ")
#     mproc2 = Process(target=compute_pi, args=(200000,))
#     mproc2.start()
#     mproc2.join()
#     print("second process compelted")


# if __name__ == '__main__':
#     mypi = compute_pi(100000)
#     print("My Pi : {0}, Error: {1} ".format(mypi, mypi - pi))

# def start_function_for_process(n):
#     time.sleep(0.2)
#     result = n*n 
#     return result

# if __name__ == '__main__':
#     p = Pool(5)
#     result = p.map(start_function_for_process,range(200),chunksize=10)
#     print(result)
#     p.close()

def ponger(p,s):
    count = 0 

    while count < 10:
        msg = p.recv()
        print("process {0} got message {1}".format(os.getpid(),msg))
        time.sleep(1)
        p.send(s)
        count +=1
    
if __name__ == '__main__':
    parent, child = Pipe()
    proc = Process(target=ponger,args=(child,'ping'))
    proc.start()
    parent.send('wonging')
    ponger(parent,'pong')
    proc.join()


        