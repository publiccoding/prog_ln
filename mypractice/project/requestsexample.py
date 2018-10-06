import requests

url = "http://maps.googleapis.com/maps/api/geocode/json"
loc = "delhi technological university"
params = {'address':loc}

r = requests.get(url = url, params= params)

##data = r.json()

print(r.text)
print(r.json())
print(r.encoding)
