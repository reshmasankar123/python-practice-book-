import os
import os.path, time
#def extcount("dir"):
for path, subdirs, files in os.walk('/home/reshma/Desktop'):
    	for filename in files:
    		print filename
    		print time.ctime(os.path.getmtime(filename))
    		print time.ctime(os.path.getctime(filename))
