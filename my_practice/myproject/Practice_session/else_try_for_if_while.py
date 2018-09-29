


# in the for loop else will execute if break condition fails or not called 

for i in range(10):
    if i == 10:
        break
else:
    print("thimmarayan k")

# in the for loop else will execute if the exception not occures

try: 
    a = 10/1
except ZeroDivisionError as e:
    print(e)
else:
    print("if exception not occured ")
finally :
    print('this will called always')