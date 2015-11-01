from sys import stdout, stdin
from math import sqrt,acos
PI = 3.1415926
in_line = stdin.readline().split()
number_of_nails = int(in_line[0])
radius = float(in_line[1])
nails = []
for i in xrange(number_of_nails):
	nails.append([float(x) for x in stdin.readline().split(' ')])
nails.append(nails[0])

length = 0
for i in xrange(len(nails) - 1):
	point1 = nails[i]
	point2 = nails[i + 1]
	length = length + sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
length = length + 2*PI*radius
print '{:.2f}'.format(length)