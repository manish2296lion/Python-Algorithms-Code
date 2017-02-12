x=100
x="{:08b}".format(x)
y=x[4:]
x=y+x[0:4]
print int(x,2)