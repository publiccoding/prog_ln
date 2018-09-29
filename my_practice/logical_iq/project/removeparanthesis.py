
def checkParanthesis():
   
    stack= []
    stack_dic = {}
    count=0
    with open('test.java') as file:
        
        for i,line in enumerate(file):
            
            # if empty line and excpet "{ or } " continue  
            #print(len(line))
            
            if line == '\n' or ( '{' not in line and '}' not in line):
                continue
            elif "{" in line:
                #print(line.find('{'))
                count = count + 1
                stack_dic[line.find('{')] = i+1             
            elif "}" in line:
                for i in range(len(stack_dic)-1):
                    if stack_dic.keys()[-1] == line.find('}'):
                        print('equal')
                        
                #print(line.find('{'))
            
        print(stack_dic)
                #stack_dic[i]=(line.find('{'))
                #stack.append(line.find('{'))
            # elif count!=0 and "}" in line and stack[-1] == line.find('}'):
            #     print('block found',str(i+1))
            #     stack.pop()
            #     count = count - 1               
            # else:
            #     print('match not found line number'+str(i+1)+'block number'+str(count))
                
    #print(stack,count)        
checkParanthesis()


