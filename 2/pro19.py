def head():
  print "head"
  f = open("she.txt", "r")
  l=len(open("she.txt").readlines())
  m=[None]*10
  i=0
  while(i<10):
     m[i]=f.readline()
     i=i+1
  for i in range(len(m)):
     print m[i],
def tail():
  print "tail"
  l=open("she.txt").readlines()
  print "".join(l[-10:]),
head()
tail()
