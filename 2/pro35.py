def anagrams(list):
        from itertools import permutations
        s={}
        while len(list)>0:
                x1=list.pop()
                s[x1]=s.get(x1,[])
                s[x1].append(x1)
                i=0
                while i<len(list):
                        z1=list[i]
                        perm=[''.join(p) for p in permutations(x1)]
                        if z1 in perm:
                                list.remove(z1)
                                s[x1].append(z1)
                        else:i=i+1
        return s.values()
print anagrams(['tae','souep','eat','ihba','node','peuos','ate','abhi','bhia','done','tea','soupe'])