def validation(string):
	if 'X' not in string:
		print('Строка не является уравнением.')
		return None
	arr = string.split()
	for i in arr:
		if 'X' in i:
			if '^' not in i:
				return None
			if i.count('X') > 1:
				return None
		else:
			if ('*' in i or '/' in i or '+' in i or '-' in i) and len(i) > 1:
				return None
			elif not ('*' in i or '/' in i or '+' in i or '-' in i or '=' in i) and not i.isnumeric() and not '.' in i:
				return None
	return arr