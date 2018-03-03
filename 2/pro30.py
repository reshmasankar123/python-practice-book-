import csv
import sys
f = open("a.txt", 'r')
reader = csv.reader(f)
for row in reader:
	print row
f.close()