from sys import stdout, stdin

N = int(stdin.readline())
database = [0 for x in xrange(5001)]
for i in xrange(N):
	x = int(stdin.readline())
	database[x] = database[x] + 1

keys = [0]
freq = [0]
total = 0
for i in xrange(5001):
	if(database[i] != 0):
		keys.append(i)
		database[i] = database[i] + total
		total = database[i]
		freq.append(database[i])

def find_key(index):
	for i in xrange(len(freq) - 1):
		if ((index >= freq[i]) and (index < freq[i+1])):
			return keys[i+1]

if (stdin.readline() == '###\n'):
	K = int(stdin.readline())
	for i in xrange(K):
		j = int(stdin.readline()) - 1
		stdout.write(str(find_key(j)) + '\n')
