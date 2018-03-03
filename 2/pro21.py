import sys
def wrap(filen):
  #f=open(file,"r")
  w=int(sys.argv[2])
  #print w
  wl=w
  c=0
  str=[None]*4
  f=open(filen)
  l=len(open(filen).readlines())
  #print "".join(l[-10:]),
  for i in range(l):
    str[i]=f.readline()
  for j in range(l):
    l=len(str[j])
    if(l<w):
      print str[j]
    else:
      i=0
      while(i<w):
        print str[j][i],
        i=i+1
      print ''
      while(i<l):
        print str[j][i],
        i=i+1
    w=wl
filename= sys.argv[1]

wrap(filename)
#def wrap(filename):
 #k = int(sys.argv[2])
 #f=open(filename).readlines()
 #for i in f:
  #new=i
  #while len(new)>k:
   # print new[:k]
    #new=new[k:]
  #print new
#import sys

#wrap(sys.argv[1])

