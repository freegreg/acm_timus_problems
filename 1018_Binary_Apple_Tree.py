from sys import stdout, stdin
from Queue import Queue

input = stdin.readline().split()
number_of_points = int(input[0])
Q = int(input[1])

L = [[] for x in xrange(100)]
W = [[] for x in xrange(100)]
memo = [[-1 for x in xrange(101)] for x in xrange(101)]

for i in xrange(number_of_points - 1):
	input = stdin.readline().split()
	L[int(input[0])-1].append(int(input[0])-1)
	L[int(input[1])-1].append(int(input[1])-1)
	W[int(input[0])-1].append(int(input[2]))
	W[int(input[1])-1].append(int(input[2]))
print L, W
print L, W
def solve(cur, prev, q):
	if (q==0):
		return 0
	
	if(memo[cur][q]==-1):
		g = len(L[cur])
		memo[cur][q] = 0

		if(g>1):
			i = g - 1
			while(i >= 0):
				if(L[cur][i]==prev):
					i = i - 1
					continue
				j = i - 1
				while(j >= 0):
					if(L[cur][j]==prev):
						j = j - 1
						continue
					for k in xrange(q+1):
						memo[cur][q] = max(memo[cur][q],(0 if k==0 else W[cur][i]+solve(L[cur][i],cur,k-1))+(0 if k==q else W[cur][j]+solve(L[cur][j],cur,q-k-1)))
						print memo[cur][q]
					j = j - 1
				i = i - 1
	return memo[cur][q]

print solve(0,-1,Q)