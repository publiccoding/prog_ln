import os


fh = open('popdata.txt','r')
##fh.write('this is seconde line of th file')
##fh.writelines(['this is third line\n','this will be the fourth line'])
##fh.close()
              
# Readline operation on the file

##line = file.readline()
##while line:
##    print(line.split())  
##    line = file.readline()
##file.close()
##
while True:
    line = fh.readline()
    print(line)
    if not line:
        break

fh.close()

    
        
