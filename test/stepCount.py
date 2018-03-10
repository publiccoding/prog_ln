
import json 
import datetime

def avgSteps(step):
    stepcount = retriveval()
    date =datetime.datetime.now().strftime('%Y-%b-%d')
    stepcount[date]['steps']
    if stepcount is None:
        stepcount = []
        stepcount.append(step)
    else:
        stepcount.append(step)  
    return stepcount
def retriveval():
    with open('healthstore.json') as file:
        jsondata = json.load(file)
    return jsondata

    
