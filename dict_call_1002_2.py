from sys import stdin, stdout

def word_to_nubmer(word):
	vac = ('oqz', 'ij', 'abc', 'def', 'gh ', 'kl', 'mn', 'prs', 'tuv', 'wxy')
	number = []
	for c in word:
		for i in xrange(10):
			if c in vac[i]:
				number.append(i)
				break
	return number
	
print word_to_nubmer('realityour')

tests_list = []
line = stdin.readline()
while(line != '-1'):
	dict = {}
	dict['number'] = line
	dict['dict_length'] = int(stdin.readline().split())
	dict['dict_words'] = []
	dict['dict_numbers'] = []
	for x in xrange(dict['dict_length'] + 1):
		word = stdin.readline()
		dict['dict_words'].append(word)
		dict['dict_numbers'].append(word_to_nubmer(word))
	tests_list.append(dict)
	line = stdin.readline()
	
print tests_list