from sys import stdout, stdin

N = int(stdin.readline())
K = int(stdin.readline())

F = [0 for x in xrange(N)]

F[0] = K-1
F[1] = K*F[0]
i = 2
while(i < N):
	F[i] = (K-1) * (F[i-1]+F[i-2])
	i = i + 1

print F[N-1]