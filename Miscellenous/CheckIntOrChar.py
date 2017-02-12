print "Enter your number"
n=raw_input()
x=False
try:
	d=int(n)
	x=True
except:
	x=False

if x == True:
	print "Integer"
else:
	print "Character"