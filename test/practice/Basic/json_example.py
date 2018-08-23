
import json 


data_json = {"name":"thimmarayan","age":25,"address":["Varaganappalli","Denkanikottai","Krishnagiri"]}

# JSON dumps example 
my_data = json.dumps(data_json)  # takes dictonay object and product string 
print(type(my_data))
print(my_data)

#JSON loads example 
my_data1 = json.loads(my_data) # takes string object and product dictonay
print(type(my_data1))
print(my_data1)

# JSON dump example 

with open('data.json','w') as f:
	data = json.dump(data_json,f)
print(data)

with open('data.json','r') as f:
	data = json.load(f)
data_value=(x for x in data['address'])
for i in data_value:
	print(i)




