import re


def is_valid_number(string: str):
    match_compile = re.compile(r'\A[-\s]?(\d+|(\d+(.|,)\d+))$')

    if match_compile.match(string=string):
        return True
    else:
        return False


def is_valid_sign(string: str):
    match_compile = re.compile(r'[-+=*]$')

    if match_compile.match(string=string):
        return True
    else:
        return False


def is_valid_x(string: str):
    match_compile = re.compile(r'([Xx]|[Xx]\^[0-2])$')

    if match_compile.match(string=string):
        return True
    else:
        return False