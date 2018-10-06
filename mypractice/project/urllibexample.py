import urllib.request

url = "http://www.google.com/"
req = urllib.request.Request(url)
res = urllib.request.urlopen(req)
print(res.read()))
