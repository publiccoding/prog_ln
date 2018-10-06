import json

json_data = {'name':'thimmarayan','addr':['varaganappalli','bangalore'],'mob':'9845991661'}

dumps_data = json.dumps(json_data)
print(dumps_data)


# dump data into json file

with open('out.json','w') as file:
    json.dump(json_data, file)


loads_output = json.loads(dumps_data)

print(type(loads_output))

data_out = json.load("test.json")
print(data_out)
data_out.close()




##print(val)
##print(data)



    
