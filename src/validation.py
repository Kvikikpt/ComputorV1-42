from src import reduced


def validation(string):
	if 'X' not in string or '=' not in string:
		print('The string isn\'t a polynomial equation')
		return None
	arr = string.split()
	for i in arr:
		if 'X' in i:
			if '^' not in i:
				print('Incorrect parameter format')
				return None
			if i.count('X') > 1:
				print('Incorrect parameter format')
				return None
			for letter in i:
				if letter.isnumeric():
					continue
				if letter == '^':
					continue
				if letter == 'X':
					continue
				print('Incorrect parameter format')
				return None
		else:
			if ('*' in i or '/' in i or '+' in i or '-' in i) and len(i) > 1:
				print('Nor right sign format')
				return None
			elif not ('*' in i or '/' in i or '+' in i or '-' in i or '=' in i) and not i.isnumeric() and not reduced.is_double(i):
				print('Incorrect number format')
				return None
	a = 0
	while a < len(arr):
		if arr[a] != '0':
			if (arr[a].isnumeric() or reduced.is_double(arr[a])) and arr[a + 1] != '*':
				print('Incorrect parameter format')
				return None
		if '=' in arr[a] and a + 1 >= len(arr):
			print('There\'s no expression after \'=\' symbol')
			return None
		if 'X' in arr[a] and (a == 0 or a == 1):
			print('Incorrect parameter format')
			return None
		if 'X' in arr[a] and (arr[a - 1] != '*' or (not arr[a - 2].isnumeric() and not reduced.is_double(arr[a - 2]))):
			print('Incorrect parameter format')
			return None
		a += 1
	return arr
