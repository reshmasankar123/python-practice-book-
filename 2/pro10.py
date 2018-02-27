def unique(n):
      l=len(n)
      m=[]
     
      for i in n:
         if i not in m:
            m.append(i)
      print m
         
unique([1,2,3,1,3,4,3,3,3,1,8,9])


#for j in range(l):
 #              if(m[j]==n[i]):
  #                count=count+1
   #      if(count==1):
    #            print n[i],
