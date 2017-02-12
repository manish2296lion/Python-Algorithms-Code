testCases=int(raw_input())
for _ in xrange(testCases):
    d=dict()
    n=int(raw_input())
    d[0]=1
    d[1]=1
    sum=0
    for i in xrange(2,n+1):
        d[i]=0
        for j in xrange(0,i):
            d[i]=d[i]+d[j]*d[i-j-1]
    print d[n]