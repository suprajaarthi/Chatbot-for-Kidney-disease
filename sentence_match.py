import re
text="Hey guyz how! do you do"
pattern =r'[;,\s]'
res=re.split(pattern,text)
print(res)

# ['Hey', 'guyz', 'how!', 'do', 'you', 'do']
