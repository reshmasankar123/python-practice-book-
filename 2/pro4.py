def pdt(a):
  l=len(a)
  pdt=1
  for i in range(l):
    pdt=pdt*a[i]
  return pdt
s=pdt([5,2,3])
print s
