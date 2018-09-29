import re
import urllib.request
import pickle

uri ="http://www.pythonchallenge.com/pc/def/banner.p"
data = pickle.load(urllib.request.urlopen(uri))

for line in data:
    print("".join([k * v for k, v in line]))