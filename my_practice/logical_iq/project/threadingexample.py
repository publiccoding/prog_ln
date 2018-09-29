import threading 
import time
import numpy as np 


# threading Basic functionality 


def do_this():
    
    #global dead
    x=0
    print("this is our thread called")
    while( not dead ):
        x +=1
        pass

    print(x)
     

def do_before():
    
    global x
    while(x < 300):
        time.sleep(.001)
        x +=1
    if x == 300:
        print(x)
        
         
def do_after():
    global x
    x=450
    while(x < 600):
        x +=1
    print(x)
    while(True):
        pass


def main():

    global dead
    dead = False
    global x 
    x=0

    main_thread = threading.enumerate()[0]
    print(main_thread.isDaemon())

    # our_thread = threading.Thread(target=do_this, name="OurThread")
    # our_thread.start()
    # print(our_thread.is_alive())
    
    our_before = threading.Thread(target=do_before)
    #our_before.setDaemon(True)
    our_before.start()
    print(our_before.isDaemon())

    our_after = threading.Thread(target=do_after)
    our_after.setDaemon(True)
    our_after.start()
    print(our_after.isDaemon())
 

    print(threading.active_count())
    print(threading.enumerate())
    print(threading.current_thread())
    print(threading.main_thread())
    print(threading.get_ident())

    # print(input("hit Enter to exit"))
    # dead = True
    
    print(our_before.is_alive())
    print("Enter again to to exit ")
    print(our_after.is_alive())

if __name__ == '__main__':
    main()

# class myThread(threading.Thread):

    
#     def __init__(self,msg,num,data=None):
#         threading.Thread.__init__(self)
#         self.msg = msg
#         self.num = num 
#         self.data = data
  
#     def run(self):
#         tlock = threading.Lock()
#         if self.data is None:
#             self.data = []
#         print("lock acquired")
#         tlock.acquire()
#         try:
#             for i in range(self.num):
#                 time.sleep(0.2)
#                 self.data.append(self.msg)
#             print(self.data)
#         except IndexError as e:
#             print(e)
#         print("Lock released")
#         tlock.release()
# if __name__ == '__main__':
#     t1 = myThread('thimma',10)
#     t1.start()
#     t1.join()
#     print("exiting main program")


def pushvalue(file,n,stack):
    with open(file) as file:
        for line in file:
            stack.append(line)
              
    # for i in range(n):
    #     print("i am pussing")
        
def popValue(file,n,stack):

     with open(file,'w') as file:
         for data in range(len(stack)):
             file.write(stack.pop())         
             
    # for i in range(n):
    #     print("i am poping ")
    #    time.sleep(n)


if __name__ == "__main__":
    stack = []
    t1 = threading.Thread(target=pushvalue, args=('pushdata.txt',0.0, stack))
    t1.start()
    t1.join()
    print(stack)
    t2 = threading.Thread(target=popValue, args=('popdata.txt',1, stack))
    t2.start()
    t2.join()
        
    print(stack)
    
print("maint thread exit")