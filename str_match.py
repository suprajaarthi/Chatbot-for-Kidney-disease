import re
string = "Tiger is the national animal of india"
pattern ="Tiger"
res=re.match(pattern,string).group(0)
print(res)