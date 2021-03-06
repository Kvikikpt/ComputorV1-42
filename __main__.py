#!/usr/bin/env python3
import sys
from src import validation
from src import reduced
from src import do
from src import check

a = 0
flag = 0
prec = 6
while a < len(sys.argv):
    if '-p' in sys.argv[a]:
        try:
            prec = int(sys.argv[a + 1])
            flag += 2
            a += 1
        except:
            print('Nor right usage of flag -p')
            exit(1)
    a += 1

if len(sys.argv) == 2 + flag:
    arr = validation.validation(sys.argv[1 + flag])
    if arr is not None:
        arr = reduced.reduced_form(arr, prec)
        # todo какая то хуйня выводится:
        # array : ['-5', '*', 'X^1', '=', '1', '*', 'X^0']
        # Reduced form: -5 -5 * X^1 - 1 * X^0 = 0
        print_reduced = ''
        for a in arr:
            print_reduced += a + ' '
        print(f'Reduced form: {print_reduced}= 0')
        degree = check.check_degree(arr)
        print(f'Polynomial degree: {degree}')
        if degree > 2:
            print('The polynomial degree is stricly greater than 2, I can\'t solve.')
        else:
            x = reduced.fill_x_array(arr, degree)
            if x[0] == 0 and x[1] == 0 and x[2] == 0:
                print('Any value will be a solution')
            elif x[1] == 0 and x[2] == 0:
                print('There is no possible solutions')
            else:
                if degree == 2 and x[2] != 0:
                    if x[1] == 0:
                        print('There\'s no solutions')
                    do.exec_square(x, prec)
                if degree == 1 or (degree == 2 and x[2] == 0):
                    do.exec_simple(x)
                if degree == 0:
                    print('The only solution is 0')
else:
    print('usage: [flags: -p] + [flags parameters if needed for: -p] [polynomial equation]')


# ((\d+|\d+(\.|,)\d+)\s\*\sX\^[0-2])+ regex