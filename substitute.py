import re
string = "Tiger is the national animal of india which is too privilegious"
pattern ="is"
no = re.sub(pattern,"was",string)
print(no)

