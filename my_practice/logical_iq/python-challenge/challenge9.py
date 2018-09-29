import bz2 
import re
import urllib.request

"""
1. To convert a string to bytes.
data = ""  			#string
data = "".encode()	#bytes
data = b"" 			#bytes
Copy
2. To convert bytes to a String.
data = b""  		#bytes
data = b"".decode() #string
data = str(b"")  	#string
"""
request = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read().decode('utf-8')
data = re.findall("\'(.*?)\'",r"".join(re.findall('<!--(.*?)-->',request,re.DOTALL)))
print(data)
un = data[0].encode()
pw = data[1].encode()

print(bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
print(bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))
