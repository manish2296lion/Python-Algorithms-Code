# ql=[1,0,0,0,1,1,0,1,0,1,1,1]

# bM=list()
# eM=list()
# m=3
# n=4
# i=0
# j=0
# for elem in ql:
# 	if(i==m):
# 		i=0
# 		j=j+1
# 		bM.append(eM)
# 		eM=[]
# 	eM.append(elem)	
# 	i=i+1
# bM.append(eM)	


booleanMatrix=[[1,0,0,1,0],
							 [0,1,0,1,1],
							 [1,1,1,1,0],
							 [0,0,0,1,0],
							 [1,1,0,1,1]]
							 
d=dict()
def findAdj(matrix,x,y):
	cords_adj=[]
	flag=False
	z=[0,1,-1]
	for p in z:
		for q in z:
			if(p==0 and q==0):
				continue
			try:	
				if(matrix[x+p][y+q]==1):
					if (x+p<0 or y+q<0):
						continue
					cords_adj.append((x+p,y+q))
			except IndexError:
				pass
	return cords_adj

for i in xrange(len(booleanMatrix)):
	for j in xrange(len(booleanMatrix[0])):
		if booleanMatrix[i][j]==1:
			d[(i,j)]=findAdj(booleanMatrix,i,j)
			print "{} s {}".format((i,j),d[(i,j)])


		
queue=[]
lengthVals=dict()
parentVals=dict()
visited=dict()
for o in list(d.keys()):
	visited[o]=False
def bfs(Source,d):
	lengthVals[Source]=0
	visited[Source]=True
	for child in d[Source]:
		parentVals[child]=Source
		visited[child]=True

	queue.extend(d[Source])
	while not len(queue)==0:
		currentElem=queue.pop(0)
		lengthVals[currentElem]=lengthVals[parentVals[currentElem]]+1
		for child in d[currentElem]:
			if(not visited[child]==True):
				visited[child]=True
				parentVals[child]=currentElem
				queue.append(child)		

bfs((0,0),d)	
# print lengthVals
XM=[1,0]
try:
	print lengthVals[(XM[0],XM[1])]

except:
	adjZero=findAdj(booleanMatrix,XM[0],XM[1])
	lnAdj=[lengthVals[elm] for elm in adjZero]
	print min(lnAdj)+1

	











