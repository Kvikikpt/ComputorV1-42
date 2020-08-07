from src import reduced
from .utils import is_valid_number, is_valid_sign, is_valid_x


def validation(string):
    if 'X' not in string or '=' not in string:
        print('The string isn\'t a polynomial equation')
        return None

    arr = string.split()

    for i in arr:
        if is_valid_number(i):
            continue
        elif is_valid_sign(i):
            continue
        elif is_valid_x(i):
            continue
        else:
            print('Not matched the regexp regular expression')
            return None

    a = 0
    while a < len(arr):
        if arr[a] != '0':
            if is_valid_number(arr[a]) and a + 1 >= len(arr):
                arr = arr[0:a] + [f'{arr[a]}'] + ['*'] + ['X^0'] + arr[a + 1:]
                continue
            if is_valid_number(arr[a]) and (arr[a + 1] == '-' or arr[a + 1] == '+' or arr[a + 1] == '='):
                arr = arr[0:a] + [f'{arr[a]}'] + ['*'] + ['X^0'] + arr[a + 1:]
                continue
            elif is_valid_number(arr[a]) and arr[a + 1] != '*':
                print('Incorrect parameter format8')
                return None
        if '=' in arr[a] and a + 1 >= len(arr):
            print('There\'s no expression after \'=\' symbol')
            return None
        if ('X' in arr[a] or 'x' in arr[a]) and (a == 0 or a == 1):
            arr[a] = 'X'
            arr = arr[0:a] + ['1'] + ['*'] + [f'{arr[a]}'] + arr[a + 1:]
            continue
        if ('X' in arr[a] or 'x' in arr[a]) and (arr[a - 1] != '*' or not is_valid_number(
                arr[a - 2])):
            arr[a] = 'X'
            arr = arr[0:a] + ['1'] + ['*'] + [f'{arr[a]}'] + arr[a + 1:]
            continue
        a += 1
    print(arr)
    return arr
