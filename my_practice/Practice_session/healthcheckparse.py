
import collections 

util = []

with open(r'C:\Users\kristhim\Desktop\work plan\2018\healthcheck\utility.txt') as utility:
    for u in utility:
        util.append(u)
    
        
with open(r'C:\Users\kristhim\Desktop\work plan\2018\healthcheck\Betagro\hp4prdhdb\rpm.txt') as file:
    for f in file:
        for u in util:
            # print(f)
            # print(u.strip())
            if u.strip() in f and '(none)' in f:
                print(f)
                
                
    

            
                          
