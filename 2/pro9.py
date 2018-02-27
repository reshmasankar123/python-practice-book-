def cumlpdt(n):
 l=len(n)
 m=[]
 pdt=1
 for i in range(l):
   pdt=pdt*n[i]
   m.append(pdt)
 print m
cumlpdt([1,2,3,4])
