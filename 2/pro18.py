def revline():
 f = open("she.txt", "r")
 s = f.read()
 f.close()
 f = open("she.txt", "w")
 f.write(s[::-1])
 f.close()
revline()
