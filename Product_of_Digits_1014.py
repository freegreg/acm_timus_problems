from sys import stdout, stdin

q_initial = int(stdin.readline())
if (q_initial == 0):
	stdout.write(''.join(['1', str(q_initial)]))
	exit()
slice_numbers = [9, 8, 6, 4, 2, 3, 5, 7]
digits = []
q = q_initial
while(q > 9):
	for i in slice_numbers:
		if ((q % i == 0)):
			digits.append(i)
			q = q / i
			break
	else:
		digits = ['-1']
		break
else:
	digits.append(q)
	digits.sort()
stdout.write(''.join([str(x) for x in digits]))