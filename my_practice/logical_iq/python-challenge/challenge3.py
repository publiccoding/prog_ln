import re
import urllib.request
# find rare characters in the mess below:

# problem solving approach 

# 1. find list of character is in the string by converting string to list and count the repeatable character
# 2. find the count of each character 
# 3. dispay the least count character
# find rare characters in the mess below:

data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode('utf-8')
data = re.findall("<!--(.*?)-->", data, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]",data)))
count ={}

for d in data:
    count[d] = count.get(d, 0) + 1
print(count)


# My approach
# dict = {}
# d =""
# characters = list(set(list(data)))
# print(characters)
# for val in characters:
#     if data.count(val) < 10 :
#         d = d + val.strip()
# print(d)
       

# import urllib.request

# html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode().encoding('utf-8')

# print(html)