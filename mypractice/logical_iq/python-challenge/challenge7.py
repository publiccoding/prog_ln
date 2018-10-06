import zipfile
import re 


path = "C:\\Users\\kristhim\\Downloads\\channel.zip"
f = zipfile.ZipFile(path)
num = "90052"

comments = []
while True:
    content = f.read(num + '.txt').decode('utf-8')
    comments.append(f.getinfo(num + ".txt").comment.decode('utf-8'))
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print("".join(comments))
