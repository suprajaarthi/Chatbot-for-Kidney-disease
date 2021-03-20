import re
string = "Tiger is the national animal of india"
pattern ="Tiger"
res=re.search(pattern,string).group(0)
print(res)