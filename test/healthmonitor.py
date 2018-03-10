
import datetime 
import random
import json 
import collections
import sleepmonitor
import stepCount

data = {}
colval =collections.OrderedDict()
new_dict = {}
datalist = []
date =datetime.datetime.now().strftime('%Y-%b-%d')
#today = date =datetime.datetime.now().strftime('%Y-%b-%d')
print(date)
jsondata = stepCount.retriveval()

steps = input("Enter the todays stepcount")
if date in jsondata:
    stepcount =jsondata[date]['steps']
    stepcount.append(steps)
    data['steps']=stepcount
    colval[date] = data
    with open('healthstore.json','r+') as health:
        json.dump(colval,health)
    print(stepcount)
else:
    stepcount = []
    stepcount.append(steps)
    data['steps']=stepcount
    colval[date] = data
    print(colval)
    with open('healthstore.json','r+') as health:
        json.dump(colval,health)
