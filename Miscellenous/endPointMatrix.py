state=(0,1)
matrix=[[0,0,0,1],[0,0,1,0],[1,0,1,0]]
rules={(1,0):(0,-1),(0,1):(1,0),(-1,0):(0,-1),(0,-1):(-1,0)}
i=0
j=0
def move(matrix,rules):
	global i,j,state
	# print "{},{}".format(i,j)
	if(matrix[i][j]==0):
		i=i+state[0]
		j=j+state[1]
	else:
		# print "changed" 
		state=rules[state]
		matrix[i][j]=0
		i=i+state[0]
		j=j+state[1]
		

def traverse(matrix,rules):
	global i,j,state
	try:	
		while True:
			if(i>=0 and j>=0):
				move(matrix,rules)
			else:
					break	
	except:
			pass						
	i=i-state[0]
	j=j-state[1]
	print "{},{}".format(i,j)

traverse(matrix,rules)

# move(matrix,rules,state)				
