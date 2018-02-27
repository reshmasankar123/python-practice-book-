def min(n):
  l=len(n)
  small=99999999999999
  for i in range(l):
    if(n[i]<small):
         small=n[i]
  return small  
def max(n):
  l=len(n)
  large=0
  for i in range(l):
    if(n[i]>large):
         large=n[i]
  return large
 
s=min([1,208,13,4])
la=max([1,208,13,4])
print s
print la
