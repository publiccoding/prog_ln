import requests 
from io import BytesIO
from PIL import Image 
import re

#img = Image.open("oxygen.png")

# img = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
# row = [img.getpixel((x,img.height / 2)) for x in range(img.width)]
# row = row[::7]
# ords = [r for r, g, b, a in row if r == g == b]

# nums = re.findall("\d+", "".join(map(chr,ords)))
# print("".join(map(chr,map(int,nums))))

from urllib.request import urlopen
import png 
import re 

response = urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
(w,h,rgba,dummy) = png.Reader(response).read()
it = list(rgba)
mid = int( h / 2 )
l = len(it[mid])
res = [ chr(it[mid][i]) for i in range(0,l, 4*7) if it[mid][i] == it[mid][i+1] == it[mid][i+2]]
print("".join(map(chr, map(int, re.findall('\d+',"".join(res))))))

