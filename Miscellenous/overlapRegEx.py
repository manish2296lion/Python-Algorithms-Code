import re

string="abcd100010000100001asda00101001adsad"
ptn=re.compile(r'(?=(10+1))')
result=["".join(x) for x in re.findall(ptn,string)]
print len(result)