import re
string = "Tiger is the national animal of india"
pattern ="is"
no = re.finditer(pattern,string)
for m in no: 
	print(m.start())
