import os
for root, dirs, files in os.walk('/home/reshma/Desktop'):
	level = root.replace('/home/reshma/Desktop', '').count(os.sep)
	indent = ' ' * 4 * (level)
	print('{}{}/'.format(indent, os.path.basename(root)))
	subindent = ' ' * 4 * (level + 1)
	for f in files:
		print('{}{}'.format(subindent, f))