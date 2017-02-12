testCases=raw_input()
for q in xrange(int(testCases)):
        n=int(raw_input())
        l=[int(x) for x in str(raw_input()).split(" ") if not x=='\r']
        s=dict();       #contain length of longest subsequences
        for k in xrange(len(l)):
            s[k]=1
        for i in xrange(len(l)-2,-1,-1):
            for j in xrange(i+1,len(l)):
                if(l[j]>l[i]):
                    s[i]=max(s[i],1+s[j])
        print "{}".format(max([y for x,y in s.iteritems()]))