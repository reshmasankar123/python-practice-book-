def pdt(a,b):
  return a*b
def fact(n):
   if(n==0):
       return 1
   else:
         x=range(n+1)
         for i in x[1:n]:
              x[i+1]=pdt(x[i],x[i+1])
         return x[n]
f=fact(0)
print f 
