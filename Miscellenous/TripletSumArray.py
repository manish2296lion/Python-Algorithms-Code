for _ in xrange(int(raw_input())):

    n,x=str(raw_input()).split(" ")
    x=int(x)
    string=str(raw_input()).split(" ")
    ls=[int(m) for m in string if not m=="\r" ]
    ls.sort()
    def tripSum(ls,x):
        for i in xrange(len(ls)-2):
            l=i+1
            r=len(ls)-2
            while(not l==r):
                if ls[i]+ls[r]+ls[l]==x:
                    return True
                elif ls[i]+ls[r]+ls[l]<x:
                    l=l+1
                else:
                    r=r-1
    if tripSum(ls,x)==True:
        print 1
    else:
        print 0