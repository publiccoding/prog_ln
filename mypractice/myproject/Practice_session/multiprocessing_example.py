import multiprocessing 

# print(multiprocessing.cpu_count())
# def worker(num):
#     print("worker",num)
     

# if __name__ == '__main__':
#     jobs = []
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,))
#         jobs.append(p)
#         p.start()
#         p.join()

from multiprocessing import Pool
import time

work = (["A", 5], ["B", 2], ["C", 1], ["D", 3])

def work_log(work_data):
    print(" Process %s waiting %s seconds" % (work_data[0], work_data[1]))
    time.sleep(int(work_data[1]))
    print(" Process %s Finished." % work_data[0])

def pool_handler():
    p = Pool(2)
    p.map(work_log, work)
   
if __name__ == '__main__':
    pool_handler()
