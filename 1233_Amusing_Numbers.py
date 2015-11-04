from sys import stdout, stdin

input = stdin.readline().split()
K = int(input[0])
M = int(input[1])


def brut_k(k):
	list = []
	for i in xrange(1, k+1):
		list.append(str(i))
	list.sort()
	return list
	
def minimal_postion_k(k):
	k_str = str(k)
	k_str_len = len(k_str)
	k_last = int(k_str[0])
	base1 = 0
	for i in xrange(k_str_len):
		base1 = base1 + int(k_str[0:i+1]) - 10**i
	base1 = base1 + i
	return base1 + 1
	
def minimal_postion_km(k, m):
	min_pos = minimal_postion_k(k)
	if (m == min_pos):
		return k
	elif (m < min_pos):
		return 0
	elif (k == 1):
		return 0
	diff_m = m - min_pos
	k1 = k - 1
	k1_base = 10 ** (len(str(k)) - 1)
	if(k1_base == k):
		return 0
	tmp_diff_m = diff_m
	pos = 0
	while(tmp_diff_m > (k1 - k1_base + 1)):
		tmp_diff_m = tmp_diff_m - (k1 - k1_base + 1)
		k1 = k1 * 10 + 9
		k1_base = k1_base * 10
	pos = k1_base + tmp_diff_m

	return pos

print minimal_postion_km(K, M)
