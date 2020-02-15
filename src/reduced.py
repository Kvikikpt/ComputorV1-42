def is_double(str):
	for i in str:
		if i.isnumeric():
			continue
		elif i == '.':
			continue
		return False
	return True

def sort_arr(arr):
	flag = False
	x = [1, 1, 1]
	prev_num = 0
	prev_sign = ''
	for i in arr:
		if i == '=':
			flag = True
			continue
		if not flag:
			if 'X^0' in i:
				x[0] *= float(prev_num)
				if '-' in prev_sign:
					x[0] *= -1
				prev_sign = ''
				prev_num = ''
			if 'X^1' in i:
				x[1] *= float(prev_num)
				if '-' in prev_sign:
					x[1] *= -1
				prev_sign = ''
				prev_num = ''
			if 'X^2' in i:
				x[2] *= float(prev_num)
				if '-' in prev_sign:
					x[2] *= -1
				prev_sign = ''
				prev_num = ''
			if '+' in i or '-' in i:
				prev_sign = i
			if i.isnumeric() or is_double(i):
				prev_num = i
		else:
			if 'X^0' in i:
				if '-' in prev_sign:
					x[0] -= float(prev_num)
				elif '+' in prev_sign:
					x[0] += float(prev_num)
				prev_sign = ''
				prev_num = ''
			if 'X^1' in i:
				if '-' in prev_sign:
					x[0] -= float(prev_num)
				elif '+' in prev_sign:
					x[0] += float(prev_num)
				prev_sign = ''
				prev_num = ''
			if 'X^2' in i:
				if '-' in prev_sign:
					x[0] -= float(prev_num)
				elif '+' in prev_sign:
					x[0] += float(prev_num)
				prev_sign = ''
				prev_num = ''
			if '+' in i or '-' in i or not prev_sign:
				if '-' in i:
					prev_sign = '+'
				else:
					prev_sign = '-'
			if i.isnumeric() or is_double(i):
				prev_num = i
	return x