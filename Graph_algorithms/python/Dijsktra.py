#Dijkstra
class MinHeapStructure():

	def __init__(self,Array):
		self.heap=Array[:]
		self.minHeap(self.heap)

	def swap(self,m,n,arr):
		o=arr[m]
		arr[m]=arr[n]
		arr[n]=o


	def minHeapify(self,i,arr):
		if(i <= len(arr)/2-1):
			try:
				if(arr[2*i+1].dist>arr[2*i+2].dist):
					minVal=arr[2*i+2].dist
					minInd=2*i+2
				else:
				    minVal=arr[2*i+1].dist
				    minInd=2*i+1
			except IndexError:
					minVal=arr[2*i+1].dist
					minInd=2*i+1
			if(arr[i].dist>minVal):
					self.swap(i,minInd,arr)
					self.minHeapify(minInd,arr)

	def minHeap(self,Array):
		for x in xrange(len(Array)/2-1,-1,-1):
			self.minHeapify(x,Array)


	def printHeap(self):
		print self.heap	

	def remMin(self):
		x=self.heap.pop(0)
		self.minHeap(self.heap)
		return x

	def updateVal(self,index,val):
		self.heap[index]=val
		self.minHeap(self.heap)

	def add(self,l):
		try:
			self.heap.append(l)
			self.minHeap(self.heap)
		except KeyError:
			pass	

class Vertex():
	def __init__(self,name):
		self.name=name
		self.dist=100000

	def relax(self,val):
		if(val<self.dist):
			self.dist=val

priorityQueue=MinHeapStructure([])
A=Vertex("A")
B=Vertex("B")
C=Vertex("C")
D=Vertex("D")
E=Vertex("E")
F=Vertex("F")
G=Vertex("G")

# Directed Graph

weightList={(A,B):10,(A,C):2,(B,D):3,(B,G):12,(C,E):2,(C,D):1,(G,E):2,(E,F):1,(D,B):2}
adjList={A:[B,C],B:[D,G],C:[E,D],D:[B],E:[F],F:[],G:[E]}
vertices=[A,B,C,D,E,F,G]
visited=set()

def Dijkstra(Source,vertices,priorityQueue):
	visited=set()
	Source.dist=0
	priorityQueue.add(Source)
	while not len(priorityQueue.heap)==0:
		nextElement=priorityQueue.remMin()
		# print "Added to list {}".format(nextElement.name)
		for elem in adjList[nextElement]:
			elem.relax(nextElement.dist+weightList[(nextElement,elem)])
			
		for elem in adjList[nextElement]:	
			if elem not in visited:
				visited.add(elem)
				priorityQueue.add(elem)
				
			

	for vert in vertices:
		print "Shortest Distance between {} and {} is {}".format(Source.name,vert.name,vert.dist)		
		vert.dist=100000
		# visited.=set()


for a in vertices:
	Dijkstra(a,vertices,priorityQueue)
