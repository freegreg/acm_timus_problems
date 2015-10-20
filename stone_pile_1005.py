from sys import stdin, stdout
import itertools
def find_minimal_difference_iterat(stones, number_of_stones):
	
	sum_total = 0
	for stone in stones:
		sum_total = sum_total + stone
	sum1 = 0
	sum_min_diff = sum_total
	
	stack = [0, 0]
	stack_debug = []
	i_debug = 1
	while(len(stack) > 0):
		i_pop = stack.pop()
		for i in xrange(i_pop, number_of_stones):
			print stack, stack_debug, i_debug
			i_debug = i_debug + 1
			stack_debug.append(stones[i])
			sum1 = sum1 + stones[i]
			
			sum_diff = abs(sum_total - 2 * sum1)
			
			if sum_diff == 0:
				return 0
			if sum_diff < sum_min_diff:
				sum_min_diff = sum_diff
			
			if (i < number_of_stones - 1):
				stack.append(i + 1)

				#print stack
		sum1 = sum1 - stones[i_pop - 1]
		stack_debug.append(-stones[i_pop - 1])
	return sum_min_diff

def find_minimal_difference_primitive(stones, number_of_stones):
	mask_bin = [0 for x in xrange(number_of_stones)]
	
	def bin_list_inc():
		mask = []
		i = 0
		while (mask_bin[i] != 0):
			mask_bin[i] = 0
			i = i + 1
		mask_bin[i] = 1
		for i in xrange(number_of_stones):
			if (mask_bin[i] == 1):
				mask.append(i)
		print mask_bin
		return mask
	
	sum_total = 0
	for stone in stones:
		sum_total = sum_total + stone
	sum1 = 0
	sum_min_diff = sum_total
	
	ind = 1
	while (ind < 2**number_of_stones):
		sum1 = sum([stones[x] for x in bin_list_inc()])
		sum_diff = abs(sum_total - 2 * sum1)
		if sum_diff == 0:
			return 0
		if sum_diff <= sum_min_diff:
				sum_min_diff = sum_diff
			
		ind = ind + 1 
	return sum_min_diff

def find_minimal_difference_standart(stones, number_of_stones):
	sum_total = 0
	for stone in stones:
		sum_total = sum_total + stone
	sum1 = 0
	sum_min_diff = sum_total
	i = 1
	while (i <= number_of_stones):
		gen = itertools.combinations(stones, i)
		for comb in gen:
			sum1 = sum(comb)
			sum_diff = abs(sum_total - 2 * sum1)
			if sum_diff == 0:
				return 0
			if sum_diff <= sum_min_diff:
				sum_min_diff = sum_diff
		i = i + 1
	return sum_min_diff
			
number_of_stones = int(stdin.readline().rstrip())
stones = stdin.readline().rstrip().split()
del stones[number_of_stones:]
stones = map(lambda x: int(x), stones)

print find_minimal_difference_standart(stones, number_of_stones)