class Vertex():
	def __init__(self,name):
		self.name=name
visited=set()

A=Vertex("A")
B=Vertex("B")
C=Vertex("C")
D=Vertex("D")
E=Vertex("E")
F=Vertex("F")
G=Vertex("G")

sequence=list()

vertices=[E,G,C,F,A,B,D]

adjList={A:[C],B:[C,E],C:[D],D:[F],E:[F],F:[G],G:[]}

def visitVertex(Vertex):
	visited.add(Vertex)
 	for v in adjList[Vertex]:
		if(v not in visited):
			visitVertex(v)
	sequence.append(Vertex)
	print Vertex.name		

for vert in vertices:
		if vert not in visited:
			visitVertex(vert)