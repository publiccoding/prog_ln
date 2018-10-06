import pickle

#print(help(pickle))


data = {'name':'thimmarayan','addr':'varaganappalli'}

pickle_file = open('test.pickle','wb')
pickle.dump(data, pickle_file)
pickle_file.close()


file = open('test.pickle','rb')
data1 = pickle.load(file)
print(type(data))
print(data1)

file.close()


