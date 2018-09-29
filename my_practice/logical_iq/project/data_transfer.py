import time
# implement recursion technique to push and pull the data

if __name__ == '__main__':
    stack = list()
    flag = True
    file = open('pushdata.txt')
    while True:
        line = file.readline()
        if not line:
            break
        elif len(stack) < 5 and flag:
            stack.append(line)
        elif len(stack) > 0:
            flag = False
            for i in range(len(stack)):
                print(stack.pop())
                print('value poped')
            time.sleep(5)
            flag = True           
    print(stack)    
