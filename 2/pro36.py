mydict = {'x':1,'y':2,'a':3}
for key in sorted(mydict.iterkeys()):
    print "%s: %s" % (key, mydict[key])