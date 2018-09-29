import urllib.request
import re


data = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode('utf-8')
data = re.findall("<!--(.*?)-->", data, re.DOTALL)[-1]
value =re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+",data)
print(value)