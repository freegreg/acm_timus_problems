from sys import stdin, stdout
import itertools

number_of_groups = int(stdin.readline())
groups = [int(x) for x in stdin.readline().split()]
groups.sort()
minimum_effect_supporters = 0
for i in range(number_of_groups/2 + 1):
	minimum_effect_supporters = minimum_effect_supporters + groups[i]/2 + 1
stdout.write(str(minimum_effect_supporters))