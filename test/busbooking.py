

import sys

#arg1=sys.argv[1]

# Register user for bus booking and stor the data in userdata.txt file 

reg = input("Enter your options :\nUser Registartion -> 1 \nUser Login -> 2\n" )

if reg == "1":
    uname = input("Enter your username")
    pwd = input("Enter your password ")
    userloginData = f' {uname} = {pwd} \n'
    with open ('userdata.txt','a') as file:
        file.write(userloginData)

# User login by validating username and password
    
elif reg == "2":
    username = input("Enter login username")
    password = input("Enter password of the user")
    logindata = {}
    with open('userdata.txt','r') as file:
        userdata = file.readlines()
        data = [data.strip().split('=') for data in userdata]
        for data in data:
            logindata[data[0]] = data[1]
            
        if username in logindata:
            if logindata[username] == password:

                
                print("login successfully")
                exit(0)
        print("Login unsuccessfull")
        exit(1)
