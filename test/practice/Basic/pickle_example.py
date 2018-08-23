import pickle 

example_dict = {1:"6",2:"2",3:"f"}

# Store object into pickle file 
file = open('pickle_test','wb')
pickle.dump(example_dict,file)
file.close()

# Read object from pickle file 
data = pickle.load(open('pickle_test','rb'))
print(data)