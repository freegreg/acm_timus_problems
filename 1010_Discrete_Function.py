from sys import stdout, stdin

N = int(stdin.readline())

k_stored = 0
i_stored = 0
f1_stored = 0
f1 = int(stdin.readline())
for i in xrange(N - 1):
	f2 = int(stdin.readline())
	k = abs(f2 - f1)
	if (k > k_stored) or ((k_stored == k) and (f1_stored < f1)):
		i_stored = i
		k_stored = k
		f1_stored = f1
	f1 = f2

print i_stored + 1, i_stored + 2
		