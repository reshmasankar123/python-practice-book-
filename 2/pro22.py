import textwrap
import sys
def wordwrap(file):
 w=int(sys.argv[2])
 f=open(file)
 strs =f.read() 
 print(textwrap.fill(strs, w))
name=sys.argv[1]
wordwrap(name)
