
text_search=''' 
abcdefMKLJSDFLKJJK 
ABCDEGHIJKLIMN 

Ha HaHa 

+919845991661
919845991661
9845991661
788.453.2342
792-255-2235
724-255-235
72-255-2352
721-25-2352
MetaCharater (Need to be escaped ):
. ^ $*+?{}[]\|()

coreyms.com
thimma.com
lakshmi.co-in
kumar.co.uk.in

'''
import re 

with open('apache_clf.txt','r') as file:
    data = file.read()
    #pattern = re.compile('\d{3}[\.-]\d{3}[\.-]\d{4}')
    #pattern = re.compile('.*?((\+91)?\d{10}).*?([a-zA-Z-._]+@[a-zA-Z-._]+).*?((https?://|www.)+?[a-zA-Z0-9-._]+)')
    #pattern = re.compile('([^\s].*) (- -) \[(.*) (.*)\].*?([A-Z]+)\s\/([a-z.]+)\s([A-Z0-9\/.]+).*?')
    pattern = re.compile('([^\s].*) (- -) \[(.*) (.*)\].*?\/([\w.]+)\s([A-Z0-9\/.]+).*?(\d+)\s(\d+).*?(https?://[a-zA-Z0-9-._]+).*?([\w\d\/.]+).*?\(([^\s].*)\)\s?([\w\d\/]?.*)')
    #pattern = re.compile('([^\s].*)\t(\w+)\t(\d+)\s(\w+)\s(\w+)')
    match = pattern.findall(data)
    #print(match)
    for mat in match:
        print(mat[2])
        # for i in range(0,len(mat),2):
        #     print(mat[i])




    





























