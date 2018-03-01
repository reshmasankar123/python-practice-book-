def rev():
  f=open("she.txt","r")
  i=0
  l=len(open("she.txt").readlines())
  m=[None]*l
  while(i<l):
        m[i]=f.readline()
        i=i+1
  while(i>0):
        i=i-1
        m[i]=m[i].strip()
        print m[i]
rev()
