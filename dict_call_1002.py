from sys import stdin, stdout

def word_to_nubmer(word):
	vac = ('oqz', 'ij', 'abc', 'def', 'gh ', 'kl', 'mn', 'prs', 'tuv', 'wxy')
	number = []
	for c in word:
		for i in xrange(10):
			if c in vac[i]:
				number.append(str(i))
				break
	return ''.join(number)

def find_shortest_seq(number, words):
	list_words = []
	word_t = []
	
	def find_seq(number, words):
		if len(number) > 0:
			for wn in words:
				if wn[1] == number[:len(wn[1])]:
					word_t.append(wn[0])
					find_seq(number.replace(wn[1], ''), words)
					del word_t[-1]
		else:
			list_words.append(' '.join(word_t))
			
	find_seq(number, words)
	
	if len(list_words) == 0:
		return 'No solution.'
	else:
		list_words.sort()
		return list_words[-1]

def find_shortest_iterat_seq(number, words):
	list_words = []
	word_t = []
	word_number_t = []
	stack = [0]
	number_t = number
	word_t_min = []
	while(len(stack) > 0):
		stack_i = stack.pop()
		len_word_t_min = len(word_t_min)
		if ((len_word_t_min == 0) or (len(word_t) + 1 < len_word_t_min)):
			for i in xrange(stack_i, len(words)):
				wn = words[i]
				wn1_len = len(wn[1])
				if wn[1] == number_t[:wn1_len]:
					stack.append(i + 1)
					word_t.append(wn[0])
					word_number_t.append(wn[1])
					number_t = number_t[wn1_len:]
					if (len(number_t) == 0):
						if (len(word_t) == 1):
							return ' '.join(word_t)
						word_t_min = word_t[:]
						number_t = word_number_t[-1] + number_t
						del word_number_t[-1]
						del word_t[-1]
					else:
						stack.append(0)
					break
			else:
				if (len(word_t) > 0):
					number_t = word_number_t[-1] + number_t
					del word_number_t[-1]
					del word_t[-1]
		else:
			if (len(word_t) > 0):
				number_t = word_number_t[-1] + number_t
				del word_number_t[-1]
				del word_t[-1]
	if (len(word_t_min) == 0):
		return 'No solution.'
	else:
		return ' '.join(word_t_min)
		
			
tests_list = []
lines = []
for line in stdin:
	lines.append(line.rstrip())
	if line == '-1':
		break
i = 0
while(lines[i] != '-1'):
	dict = {}
	dict['number'] = lines[i]
	i = i + 1
	dict['dict_length'] = long(lines[i])
	i = i + 1
	dict['dict_words'] = []
	for x in xrange(dict['dict_length']):
		word = lines[i]
		i = i + 1
		dict['dict_words'].append((word, word_to_nubmer(word)))
	tests_list.append(dict)
	line = lines[i]

for test in tests_list:
	test['dict_words'].sort(lambda x, y : len(y[0]) - len(x[0]))
	stdout.write(find_shortest_iterat_seq(test['number'], test['dict_words']) + '\n')