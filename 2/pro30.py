def parse_csv(filename):
	f=open(filename,"r")
	list1=[]
	list2=[]
	if not f:
		print "No such file"
		return 1
	else:

	    for line in f:
		    for symbol in line:
			    if symbol!='\n' and symbol!=',':
				    list1.append(symbol)
		    list2.append(list1)
		    list1=[]
        return list2
print parse_csv("a.txt")