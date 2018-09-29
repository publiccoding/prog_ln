import time
import threading 



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