def exsort(n):
  l=len(n)
  for i in range(l):
    n[i]=n[i].split('.')
  n.sort(key=lambda n:n[1])
  for j in range(l):
    n[j]=".".join(n[j])
  print n
exsort(["aa.py","m.m","b.a","v.s"])
