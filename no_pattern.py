import re
string = "Tiger is the national animal of india"
pattern1 ="Tiger"
pattern2 ="lion"
res=re.search(pattern2,string)
print(res)