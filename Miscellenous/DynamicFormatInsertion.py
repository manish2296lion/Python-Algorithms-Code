#code
for _ in xrange(int(raw_input())):
    a,b=[int(x) for x in str(raw_input()).split(" ")]
    bits=0
    # a=bin(a)
    # b=bin(b)
    # Very Important
    pad=len("{:b}".format(max(a,b)))
    b="{no:0{p}b}".format(no=b,p=pad)
    a="{no:0{p}b}".format(no=a,p=pad)
    # print(a,b)
    for i in xrange(len(a)):
        if not a[i]==b[i]:
            bits=bits+1s
    print bits    