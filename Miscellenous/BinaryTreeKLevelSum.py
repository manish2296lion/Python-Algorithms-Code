import re
s="(0(5(61()())(4()(93()())))(7(111()())(3()())))"
level=-1
d=dict()
for lvl in xrange(-1,20):
	d[lvl]=0
flag=False	
ptn=re.compile(r'^\d+')
for i in xrange(len(s)):
	if(s[i]=="("):
		level=level+1
		flag=False
	elif(s[i]==")"):
		level=level-1
		flag=False
	else:
		if(flag==False):
			number=int(re.findall(ptn,s[i:])[0])
			print "{},{}".format(number,level)
			d[level]=d[level]+number
			flag=True

print int(re.findall(ptn,s[5:])[0])
