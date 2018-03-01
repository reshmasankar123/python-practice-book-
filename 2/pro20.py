def grep(str):
  lines=open("she.txt").readlines()
  return [line for line in lines if str in line] 
print "".join(grep("sure"))
