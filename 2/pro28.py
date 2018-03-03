def enumerate(list):
	l=len(list)
	print [(x,y) for x in range(l) for y in list if y==list[x]]
enumerate([1,3,2])