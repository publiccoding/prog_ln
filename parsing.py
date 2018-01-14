# import re 

# text_search ='''
# abcdefghifslkfjadfklj
# ABCDAFDGEARAWEGGAFASDF
# 1243412798571934719278341
# thimma.com
# thimma@gmail.com
# thimmrayan@hpe.com
# thimm.rayan@hpe.com
# thimma-rayan@hpe.com
# kumar_krish@gmail.co.in
# thimma-rayan@hpe-co.in 
# https://www.thimmarayan.com
# http://www.gmail.com 
# http://thimmarayan.com 
# https://youtube.com 
# http://www.gmail.co.in
# http://www.gmail-co.in
# Ha HaHa
# 234-424-2145
# 765*876-4321
# 456.908.6574
# 800-876-4321
# 900.908.6574
# Mr. Scrahf
# Ms Davis
# Mrs. Robinson
# Mr. T
# Mr Smith
# mat 
# bat
# cat 
# pat
# '''

# fake_name='''
# Dave Martin
# 643-555-7654
# 173 Main St., Springfield RI 78907
# davemarting@bogusemail.com
# Charles Harris
# 800-555-5668
# 987 High St., Alantis VA 34075
# charlesharris@bogusemail.com
# '''
# urls='''
# https://www.thimmarayan.com
# http://www.gmail.com 
# http://thimmarayan.com 
# https://youtube.com 
# http://www.gmail.co.in
# '''

# sentence = 'Start a sentence and then bring it to an end'

from threading import Thread
from time import sleep


class myThread(Thread):

    def __init__(self, val):
        Thread.__init__(self)
        self.val = val

    def run(self):
        for i in range(self.val):
            self.myfunc(i)
        
        print(self.getName())


    def myfunc(self,v):
        sleep(v)
        print('i am called from thread run',v)
    

if __name__ == '__main__':
    t = myThread(9)
    t.setName('Thread1')
    t.start()
    t.join()

