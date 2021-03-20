import re
string = "John 34-3456 12-05-2007 , XYZ 56-4532 11-11-2011 , ABC 67-945 12-01-2009"
pattern =r'\d{2}-\d{2}-\d{4}'
res=re.findall(pattern,string);
print(res)
# ['12-05-2007', '11-11-2011', '12-01-2009']
