def cumlsum(n):
 l=len(n)
 m=[]
 sum=0
 for i in range(l):
   sum=sum+n[i]
   m.append(sum)
 print m
cumlsum([1,2,3,4])
