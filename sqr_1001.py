from sys import stdin, stdout
from math import sqrt

stdout.write('\n'.join(['{0:.4f}'.format(sqrt(float(t))) for t in stdin.read().split()[::-1]]))