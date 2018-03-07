import os

for path, subdirs, files in os.walk('/home/reshma/Desktop'):
   for filename in files:
    print filename