def lensort(n):
     l=len(n)
     li=[]
     for i in range(l):
          li.append(len(n[i]))
     for j in range(l-1):
          k=j+1
          while(k<l):
            if(li[j]>li[k]):
                temp=n[j]
                n[j]=n[k]
                n[k]=temp
                #temp=li[j]
                #li[j]=li[k]
                #li[k]=temp
            k=k+1
     for i in range(l):
          print n[i],
lensort(["a","abcd","reshma","sav","b"])
