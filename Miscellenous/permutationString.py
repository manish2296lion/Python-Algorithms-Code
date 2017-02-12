def findI(str_list):
	for i in xrange(len(str_list)-1,-1,-1):
		if i==0:
			return None
		if(str_list[i]>str_list[i-1]):
			return i-1
def findJ(i,str_list):
	for j in xrange(len(str_list)-1,i,-1):
		if(str_list[j]>str_list[i]):
			return j
def swap(i,j,str_list):
	o=str_list[i]
	str_list[i]=str_list[j]
	str_list[j]=o
def reverseList(i,str_list):
	m=str_list[0:i+1]
	m.extend(str_list[len(str_list)-1:i:-1])
	return m
string="Manish"
# reverseList(1,list(string))
str_list=sorted(list(string))
print "".join(str_list)	
while True:
	i=findI(str_list)
	if i==None:
		break
	j=findJ(i, str_list)
	swap(i,j,str_list)
	str_list=reverseList(i,str_list)
	print "".join(str_list)	
