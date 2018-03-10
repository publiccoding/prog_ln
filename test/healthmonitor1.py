

import datetime 
import random


def init():
    pass

def Averagetime(date, ttime,dtime):
    dict = {}
    l = []
    l.append()

def main():
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    starttime = input("Enter your sleep Start time on "+today+"\t:")
    endtime = input("Enter your sleep End time on "+today+"\t:")
    totaltime=(float(starttime) + float(endtime))
    realtime = int(totaltime)
    print(totaltime)
    deepsleep = totaltime - random.randint(int(realtime/1.10), int(realtime-1.5) ) 
    print(deepsleep)
    Averagetime(today,totaltime,deepsleep)



if __name__ == '__main__':
    main()