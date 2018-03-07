import os
def extcount(dir):
	for path, subdirs, files in os.walk(dir):
		for filename in files:
			#print filename
			filename=filename.split('.')
			#print filename
			if filename[1]=='py':
				print "py"
				print filename[0]
			elif (filename[1]=='txt'):
				print "txt"
				print filename[0]
			elif (filename[1]=='doc'):
				print "doc"
				print filename[0]
extcount("/home/reshma/Desktop/")

