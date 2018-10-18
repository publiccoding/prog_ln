import difflib
import sys
import collections
import operator 

total = 1000

with open('/root/prog_ln/mypractice/project/file1.txt','w') as f:
	for x in range(total):
		f.write('Line no {}\n'.format(x))

with open('/root/prog_ln/mypractice/project/file2.txt','w') as f:
	for x in range(total + 10):
		if x in (500,505,total- 2):
			continue
		f.write('Line no {}\n'.format(x))

with open('/root/prog_ln/mypractice/project/file3.txt','w') as f:
	for x in range(1002,1005):
		f.write('Line no {}\n'.format(x))


with open('/root/prog_ln/mypractice/project/file1.txt','r') as f1 , open('/root/prog_ln/mypractice/project/file2.txt','r') as f2, open('/root/prog_ln/mypractice/project/file3.txt','r') as f3:
	from_list = f1.readlines()
	to_list = f2.readlines()
	dis_list = f3.readlines() # disable data which need to be subtracted from the first file
	to_list = [a - b for a, b in zip(from_list, to_list)]
	#to_list = list(map(operator.sub, to_list, dis_list))
	#to_list = [item for item in to_list if item not in dis_list]
	diff = difflib.ndiff(from_list, to_list)
	for line in diff:
		line = line.strip()
		if line.startswith('-'):
			print(line)
		elif line.startswith('+'):
			print(line)


# HTML different output

from_file = '/root/prog_ln/mypractice/project/file1.txt'
to_file = '/root/prog_ln/mypractice/project/file2.txt'
from_lines =open(from_file,'U').readlines()
to_lines =open(to_file,'U').readlines()
diff = difflib.HtmlDiff().make_file(from_lines,to_lines, context=True, numlines=0)

with open('/root/prog_ln/mypractice/project/out_file.html','w') as out_file:
	out_file.write(diff)


