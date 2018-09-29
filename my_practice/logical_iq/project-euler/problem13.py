import re
import urllib.request

data = urllib.request.urlopen("https://projecteuler.net/problem=13").read().decode('utf-8')

val = re.findall("[\d+]{50}",data)
sum_data =0
for i, line in enumerate(val):
    if i == 10 : 
        break
    sum_data = sum_data + sum([int(i) for i in line])
print(sum_data)
