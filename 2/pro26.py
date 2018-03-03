def even(x): 
	return x%2==0
def filter(fn,list):
	print [x for x in list if fn(x)!=0]
filter(even,range(10))