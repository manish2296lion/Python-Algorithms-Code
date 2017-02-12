import time
import random
# import mem_profile

name=["Man","Ram","Gyan","Lan","Ran"]
major=["Math","Physics","Chemistry","Biology","IT"]

# print "Memory before usage is {}".format(mem_profile.memory_usage_resource())

def peopleList(num):
	return [{"id":i,"name":random.choice(name),"major":random.choice(major)} for i in xrange(num) ]

def peopleGenerator(num):
	return ({"id":i,"name":random.choice(name),"major":random.choice(major)} for i in xrange(num) )

a= time.clock()
c=peopleList(1000000)
b= time.clock()	
print "time took{}".format(b-a)