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
nails.append(nails[1])
d1_precedent = sqrt((nails[0][0] - nails[1][0])**2 + (nails[0][1] - nails[1][1])**2)
length = 0
for i in xrange(len(nails) - 2):
	point1 = nails[i]
	point2 = nails[i + 1]
	point3 = nails[i + 2]
	d1 = d1_precedent
	d2 = sqrt((point2[0] - point3[0])**2 + (point2[1] - point3[1])**2)
	d1_precedent = d2
	scalar = (point1[0] - point2[0])*(point3[0] - point2[0]) + (point1[1] - point2[1])*(point3[1] - point2[1])
	vector = d1 * d2
	d2 = (PI - acos(scalar / vector))*radius
	length = length + d1 + d2

print '{:.2f}'.format(length)