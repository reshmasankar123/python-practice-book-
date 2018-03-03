def triplet(n):
	print [(x,y,z) for x in range(n) for y in range(n) for z in range(n) if x+y==z]
triplet(5)