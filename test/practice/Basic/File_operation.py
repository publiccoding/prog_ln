

#open file and write data into it.

f = open("test.txt", "w")
f.write("This data will goes into test file \nIt's sample file operation")
f.close()

# Append data in the existing test file
f = open("test.txt", "a")
f.write("\nThis data will append at  last line")
f.close()

#Read the data from the file.

# f = open("test.txt", "r")
# a=f.read()
# print(a)
# f.close()

# try : 
# 	f = open("test.txt","r")
# 	for line in f:
# 		print(line.strip('\n'))
# except FileNotFound as e:
# 	print(e)
# finally :
# 	f.close()

# try : 
# 	f = open("test.txt","r")
# 	data =f.read()
# except FileNotFound as e:
# 	print(e)
# finally :
# 	f.close()
# print(data)



# try : 
# 	f = open("test.txt","r")
# 	data =f.readlines()
# except FileNotFound as e:
# 	print(e)
# finally :
# 	f.close()

# for da in data:
# 	print(da.split('\n'))


try : 
	f = open("test.txt","r")
	while 1:
		line = f.readline()
		if not line:
			break
		print(line.split('\n'))

except FileNotFound as e:
	print(e)
except Exception as e:
	print(e)
finally :
	f.close()
print(line)