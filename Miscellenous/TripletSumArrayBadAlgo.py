l="589 343 609 61 222 759 955 889 147 691 950 844 431 621 749 68 537 784 36 227 186 39 854 630 225 749 924 360 258 767 945 956 319 727 412 26 356 2 550 497 585 516 965 343 76 914 143 197 949 73"
# l=[1,4,45,6,10,8]
l=[int(x) for x in l.split(" ")]
l.sort()
print l
y=False
level=0;
def tripSum(l,startIndex,endIndex,x,lvl):
	global y
	if(startIndex<=endIndex):	
	 for i in xrange(len(l[startIndex:endIndex+1])-1,-1,-1):
	 	if l[i]<=x:
	 		if(l[i]==x):
	 			y=True
	 			return True
 			tripSum(l,startIndex,i-1,x-l[i],lvl+1)
	 		if(y==True and lvl==3):
		 		return True

print tripSum(l,0,len(l)-1,182,level)
# string="12 12 123 "
# print string[0:-1]	 		


# print type1