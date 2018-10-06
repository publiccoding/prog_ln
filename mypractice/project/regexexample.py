import re


text_to_search = """

abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

321-555-4321
123.[555].1234
321*555-4321
123.555*(1234)


Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mrs.Thimmarayan

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

coreyms.com

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

777 High St., King's Landing AZ 16547
667 High St., Balmora IN 82473
276 High St., Braavos‎ IL 57764
859 Cedar St., Old-town MT 31169

  """

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)

# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


pattern = re.compile(r'[\w]+')
# pattern = re.compile(r'\s') # non white space character 
# pattern = re.compile(r'\d+[\W]+?.[0-9\[\]]+.[0-9\(\)]+')
# pattern = re.compile(r'M(r|s)+\.?\s*?[A-Z]\w*')
# pattern = re.compile(r'(https?:\/\/)[\w\.\-]+')
# pattern = re.compile(r'[\w\.\-]+@[\w\.\-]+')
# pattern = re.compile(r'\d{3}\s[\w]+\s[\w\.\,\'\-]+\s[\w\.\,\'\-]+.*')
result = pattern.search(text_to_search)
print(result)
#result = re.sub('thimmarayan','thimma',"my name is thimmarayan")
#print(result)
# for data  in result:
#     print(data)