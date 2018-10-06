# Example 1.0

# class MyZeroDivision(Exception):
#     def __init__(self,msg):
#         self.msg = msg 

#     def handle(self):
#         print("Custome exception", self.msg)

# try:
#     1/0
#     raise MyZeroDivision("Trying divide by zero")
# except MyZeroDivision as e :
#     print(e.handle())

# Example 2 


"""
    This example used to through Exception when number is entered is lower or higher thant the current number.
    
"""

class Error(Exception):

    @staticmethod
    def handle(msg):
        print(" i am from ERROR",msg)
    pass 
    #print(" i am error created from exception")

class LowerException(Error):
    
    @staticmethod
    def handle(msg):
        print(" i am from lower exception", msg)
    
    pass 
    #print("you have entered lower value")

class higerException(Error):
    pass 
    #print("you have entered higher value")

def valuecheck(num):

    val = 10 
    try:
        if num < val :
            raise LowerException
               
        if num > val: 
            raise higerException

        if num == val:
            print("You entered correct number")

    except LowerException as e: 
        print(e.handle('not correct'))
        print("Lower value")
    
    except higerException as e:
        print("Higer value")
    else:
        print("i am else from try block ")
    finally:
        print("I am cloing ")

valuecheck(int(input("Enter your value")))
