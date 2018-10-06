from modules import addition

class mathsOperation():

    def __init__(self, val, readMethod):
        self.val = val 
        self.readMethod = readMethod
        
    def calcOperation(self):
        if self.val == 1:
            print("You are selected Addition")
            value=addition.addValues(self.readMethod)    
            return (value)
                   
        elif self.val == 2:
            print("You are selected Multiplication")
        elif self.val == 3:
            print("You are selected Subtraction")
        else :
            print("You are selected Division")
        
# def readValue():
#     value1 = input("Enter the value 1: ")
#     value2 = input("Enter the value 2: ")
#     return (value1,value2)

# print("Choose the Maths Operation you wnat to perform.")
# print("index"+" "+"Maths_Operation")
# print("1 Addition.")
# print("2 Multiplication.")
# print("3 Subtraction.")
# print("4 Division.")

# val = int(input("\nEnter your choice...  "))
# maths = mathsOperation(val,readValue).calcOperation()




