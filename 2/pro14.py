def unique(n):
      l=len(n)
      m=[]
     
      for i in range(l):
         if n[i].lower() not in m:
            m.append(n[i])
      print m
         
unique(["hello","world","Hello"])
