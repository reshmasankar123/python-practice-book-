def sum(a):
  l=len(a)
  sum=0
  for i in range(l):
    sum=sum+a[i]
  return sum
s=sum([5,2,3])
print s
