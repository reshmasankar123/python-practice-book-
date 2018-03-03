import sys
def center(filename):
	f=open(filename).readlines()
	x=len(max(f))
	for line in f:
		p=(x-len(line))/2
		print ' '*p+line 
center("she.txt") 