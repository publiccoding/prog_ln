# The Threading Module
# The newer threading module included with Python 2.4 provides much more powerful, high-level support for threads than the thread module discussed in the previous section.
# The threading module exposes all the methods of the thread module and provides some additional methods −
# threading.activeCount() − Returns the number of thread objects that are active.
# threading.currentThread() − Returns the number of thread objects in the caller's thread control.
# threading.enumerate() − Returns a list of all thread objects that are currently active.
# In addition to the methods, the threading module has the Thread class that implements threading. The methods provided by the Thread class are as follows −
# run() − The run() method is the entry point for a thread.
# start() − The start() method starts a thread by calling the run method.
# join([time]) − The join() waits for threads to terminate.
# isAlive() − The isAlive() method checks whether a thread is still executing.
# getName() − The getName() method returns the name of a thread.
# setName() − The setName() method sets the name of a thread.
# Creating Thread Using Threading Module
# To implement a new thread using the threading module, you have to do the following −
# Define a new subclass of the Thread class.
# Override the __init__(self [,args]) method to add additional arguments.
# Then, override the run(self [,args]) method to implement what the thread should do when started.
# Once you have created the new Thread subclass, you can create an instance of it and then start a new thread by invoking the start(), which in turn calls the run() method.

import threading 
tlock = threading.Lock()
tlock.acquire()
def square_cal(number):
	print(threading.currentThread())
	for n in number:
		print("Square Root :",n*n)
tlock.release()

tlock.acquire()
def cube_cal(number):
	print(threading.currentThread())
	for n in number:
		print("cube :",n*n*n)
tlock.release()

arr = [10,20,30,40,50]

def main():
	t1=threading.Thread(target=square_cal,args=(arr,))
	t=threading.Thread(target=cube_cal,args=(arr,),daemon=True)
	t.setName("MyThreadingExample1")
	t1.setName("MyThreadingExample2")
	t.start()
	t1.start()
	print("Program is still executing")
	print(t.is_alive())
	t.join()
	t1.join()
	print("Main program complete")

if __name__ == '__main__':
	main()

# import threading 

# class AsyncThread(threading.Thread):
# 	def __init__(self,message,output):
# 		threading.Thread.__init__(self)
# 		self.message=message
# 		self.output=output
# 	def run(self):
# 		try:
# 			f = open(self.output,'a')
# 			f.write(self.message)
# 		except Exception as e : 
# 			print(e)
# 		finally :
# 			f.close()

# message=input("Enter the value")
# mythread1 = AsyncThread(message,'output.txt')
# mythread1.start()
# print(mythread1.is_alive())
# #mythread1.setDaemon(True)
# mythread1.join()

#result = subprocess.run('echo Hello ; echo World', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
