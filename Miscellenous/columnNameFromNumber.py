d=dict()
e=dict()
d[0]=90
e[0]="Z"
for i in xrange(25):
	d[i+1]=i+65
	e[i+1]=chr(i+65)
print e
level=0
n=470211273
string=[]
while(n>0):
 	string.append(chr(d[n%26]))
 	level=level+1
	if(n%26==0):
		n=n/26-1
	else:	
 		n=n/26
string=string[::-1]
print "".join(string)
