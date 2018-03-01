def unique(n):
      l=len(n)
      m=[]
     
      for i in n:
         if i not in m:
            m.append(i)
      print m
         
def dupli(n):
     l=len(n)
     m=n[:]
     a=[]
     for i in range(l):
         count=0
         for j in range(l):
                 if(m[j]==n[i]):
                   count=count+1
         if(count!=1):
                a.append(n[i])
     unique(a)

dupli([1,2,3,1,2,5,6])
