from src import reduced


def validation(string):
	if 'X' not in string or '=' not in string:
		print('The string isn\'t a polynomial equation')
		return None
	arr = string.split()
	for i in arr:
		if 'X' in i:
			if i[0] != 'X':
				print('Incorrect parameter format1')
				return None
			if i[1] != '^':
				print('Incorrect parameter format2')
				return None
			if len(i) < 3:
				print('Incorrect parameter format3')
				return None
			if not i[2:].isnumeric:
				print('Incorrect parameter format4')
				return None
			if i.count('X') > 1:
				print('Incorrect parameter format5')
				return None
		else:
			if ('*' in i or '/' in i or '+' in i or '-' in i) and len(i) > 1:
				print('Nor right sign format6')
				return None
			elif not ('*' in i or '/' in i or '+' in i or '-' in i or '=' in i) and not i.isnumeric() and not reduced.is_double(i):
				print('Incorrect number format7')
				return None
	a = 0
	while a < len(arr):
		if arr[a] != '0':
			if (arr[a].isnumeric() or reduced.is_double(arr[a])) and a + 1 >= len(arr):
				arr = arr[0:a] + [f'{arr[a]}'] + ['*'] + ['X^0'] + arr[a + 1:]
				continue
			if (arr[a].isnumeric() or reduced.is_double(arr[a])) and (arr[a + 1] == '-' or arr[a + 1] == '+' or arr[a + 1] == '='):
				arr = arr[0:a] + [f'{arr[a]}'] + ['*'] + ['X^0'] + arr[a + 1:]
				continue
			elif (arr[a].isnumeric() or reduced.is_double(arr[a])) and arr[a + 1] != '*':
				print('Incorrect parameter format8')
				return None
		if '=' in arr[a] and a + 1 >= len(arr):
			print('There\'s no expression after \'=\' symbol')
			return None
		if 'X' in arr[a] and (a == 0 or a == 1):
			arr = arr[0:a] + ['1'] + ['*'] + [f'{arr[a]}'] + arr[a + 1:]
			continue
		if 'X' in arr[a] and (arr[a - 1] != '*' or (not arr[a - 2].isnumeric() and not reduced.is_double(arr[a - 2]))):
			arr = arr[0:a] + ['1'] + ['*'] + [f'{arr[a]}'] + arr[a + 1:]
			continue
		a += 1
	print(arr)
	return arr
