import difflib
import sys

from lxml import html 
total = 1000

# with open('/root/prog_ln/mypractice/project/file1.txt','w') as f:
# 	for x in range(total):
# 		f.write('Line no {}\n'.format(x))

# with open('/root/prog_ln/mypractice/project/file2.txt','w') as f:
# 	for x in range(total + 10):
# 		if x in (500,505,total- 2):
# 			continue
# 		f.write('Line no {}\n'.format(x))

# with open('/root/prog_ln/mypractice/project/file1.txt','r') as f1 , open('/root/prog_ln/mypractice/project/file2.txt','r') as f2:
# 	diff = difflib.ndiff(f1.readlines(), f2.readlines())
# 	for line in diff:
# 		line = line.strip()
# 		if line.startswith('-'):
# 			print(line.strip('- '))
# 		elif line.startswith('+'):
# 			print(line.strip('+ '))


# HTML different output

from_file = '/root/prog_ln/mypractice/project/file1.txt'
to_file = '/root/prog_ln/mypractice/project/file2.txt'
from_lines =open(from_file,'U').readlines()
to_lines =open(to_file,'U').readlines()
diff = difflib.HtmlDiff().make_file(from_lines,to_lines, context=True, numlines=0)

with open('/root/prog_ln/mypractice/project/out_file.html','w') as out_file:
	out_file.write(diff)


