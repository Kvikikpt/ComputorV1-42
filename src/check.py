from .utils import is_valid_number


def check_degree(arr):
    degree = -1
    last_num = 0
    for i in arr:
        if 'X' in i:
            for letter in i:
                if letter.isnumeric():
                    if int(letter) > degree and float(last_num) != 0:
                        degree = int(letter)
        if is_valid_number(i):
            last_num = i
    if degree == -1:
        for i in arr:
            if 'X' in i:
                for letter in i:
                    if letter.isnumeric():
                        if int(letter) > degree:
                            degree = int(letter)
    return degree
