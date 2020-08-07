from .utils import is_valid_number


def is_double(string): # может понадобиться потом
	for i in string:
		if i.isnumeric():
			continue
		elif i == '.':
			continue
		return False
	return True


def reduced_form(arr, prec):
	sort = []
	flag = False
	prev_num = 0
	prev_sign = None
	for i in arr:
		if i == '=':
			flag = True
			prev_sign = None
			continue
		if not flag:
			if 'X' in i:
				a = 0
				check = False
				while a < len(sort):
					if i == sort[a]:
						if '-' in prev_sign:
							num = float(sort[a-2]) - float(prev_num)
						elif '+' in prev_sign:
							num = float(sort[a - 2]) + float(prev_num)
						if num < 0:
							num *= -1
							if sort[a - 3] == '-':
								sort[a - 3] = '+'
							elif sort[a - 3] == '+':
								sort[a - 3] = '-'
						num = round(num, prec)
						if num % 1 == 0:
							num = int(num)
						sort[a - 2] = str(num)
						check = True
					a += 1
				if not check and float(prev_num) != 0:
					if prev_sign:
						sort.append(prev_sign)
					sort.append(prev_num)
					sort.append('*')
					sort.append(i)
			if '+' in i or '-' in i:
				prev_sign = i
			if is_valid_number(i): # todo из-за этой строчки валится при -5 * x
				prev_num = i
		if flag:
			if 'X' in i:
				a = 0
				check = False
				while a < len(sort):
					if i == sort[a]:
						if '-' in prev_sign and ((a - 3 >= 0 and sort[a - 3] == '+') or a - 3 < 0):
							num = float(sort[a-2]) - float(prev_num)
						elif '+' in prev_sign and a - 3 >= 0 and sort[a - 3] == '-':
							num = float(sort[a - 2]) - float(prev_num)
						else:
							num = float(sort[a - 2]) + float(prev_num)
						num = round(num, prec)
						if num % 1 == 0:
							num = int(num)
						sort[a - 2] = str(num)
						check = True
					a += 1
				if not check:
					sort.append(prev_sign)
					sort.append(prev_num)
					sort.append('*')
					sort.append(i)
			if '+' in i or '-' in i or not prev_sign:
				if '-' in i:
					prev_sign = '+'
				else:
					prev_sign = '-'
			if is_valid_number(i): # todo и из-за этой возможно тоже надо проверить короче
				prev_num = i
	i = 0
	while i < len(sort):
		if sort[i] == '0':
			if i + 2 < len(sort):
				if sort[i + 1] == '*':
					if 'X' in sort[i + 2]:
						del sort[i]
						del sort[i]
						del sort[i]
		i += 1
	return sort


def fill_x_array(arr, degree):
	x = [None, None, None]
	prev_num = ''
	prev_sign = ''
	for i in arr:
		if 'X^0' in i and degree >= 0:
			if not x[0]:
				x[0] = 1
			x[0] *= float(prev_num)
			if '-' in prev_sign:
				x[0] *= -1
			prev_sign = ''
			prev_num = ''
		if 'X^1' in i and degree >= 1:
			if not x[1]:
				x[1] = 1
			x[1] *= float(prev_num)
			if '-' in prev_sign:
				x[1] *= -1
			prev_sign = ''
			prev_num = ''
		if 'X^2' in i and degree == 2:
			if not x[2]:
				x[2] = 1
			x[2] *= float(prev_num)
			if '-' in prev_sign:
				x[2] *= -1
			prev_sign = ''
			prev_num = ''
		if '+' in i or '-' in i:
			prev_sign = i
		if '-' in i:
			if is_valid_number(i[1:]): # todo вот это хз тоже поменял мб говна подкинет
				prev_num = i[1:]
		if is_valid_number(i): # todo как и эта
			prev_num = i
	a = 0
	while a < len(x):
		if not x[a]:
			x[a] = 0
		a += 1
	print(x)
	return x
