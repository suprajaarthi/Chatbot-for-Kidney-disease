import re
string = "Tiger is the national animal of india which is too privilegious"
pattern ="is"
no = re.finditer(pattern,string)
for m in no: 
	print(m.start())
