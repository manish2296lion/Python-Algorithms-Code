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
				if(arr[2*i+1]>arr[2*i+2]):
					minVal=arr[2*i+2]
					minInd=2*i+2
				else:
				    minVal=arr[2*i+1]
				    minInd=2*i+1
			except IndexError:
					minVal=arr[2*i+1]

			if(arr[i]>minVal):
					self.swap(i,minInd,arr)
					self.minHeapify(minInd,arr)

	def minHeap(self,Array):
		for x in xrange(len(Array)/2-1,-1,-1):
			self.minHeapify(x,Array)


	def printHeap(self):
		print self.heap	

	def remMin(self):
		self.heap.pop(0)
		self.minHeap(self.heap)

	def updateVal(self,index,val):
		self.heap[index]=val
		self.minHeap(self.heap)

	def add(self,l):
		try:
			self.heap.extend(l)
			self.minHeap(self.heap)
		except KeyError:
			pass	

# Array=[12,7,6,10,8,20]
# heap=MinHeapStructure(Array)
# heap.printHeap()

