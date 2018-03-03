def square(x):return x*x
def map(fn,list):
	print [fn(x) for x in list]
map(square,range(5))