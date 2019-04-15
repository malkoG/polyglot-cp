def translate_from_suffix(word):
	if word[-2:] == 'er':
		return 'one who ' + word[:-2] + 's'
	elif word[-3:] == 'ing':
		return 'to actively ' + word[:-3]
	elif word[-3:] == 'ize':
		return 'change into ' + word[:-3]
	elif word[-1:] == 's':
		return 'multiple instances of ' + word[:-1]
	elif word[-4:] == 'tion':
		return 'the process of ' + word[:-4] + 'ing'

	return word

def translate_from_prefix(word):
	if word[:4] == 'anti':
		return 'against ' + translate_from_suffix(word[4:])
	elif word[:4] == 'post':
		return 'after ' + translate_from_suffix(word[4:])
	elif word[:3] == 'pre':
		return 'before ' + translate_from_suffix(word[3:])
	elif word[:2] == 're':
		return translate_from_suffix(word[2:]) + ' again'
	elif word[:2] == 'un':
		return 'not ' + translate_from_suffix(word[2:])
	return translate_from_suffix(word)

for i in range(int(input())):
	print(translate_from_prefix(input()))
