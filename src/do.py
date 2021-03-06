def exec_square(x, prec):
    a = x[2]
    b = x[1]
    c = x[0]

    disc = b ** 2 - (4 * a * c)
    xone = ((b * -1) - (disc ** (1 / 2))) / (2 * a)
    xtwo = ((b * -1) + (disc ** (1 / 2))) / (2 * a)
    if disc < 0:
        if xone == xtwo:
            print(f"Discriminant is strictly negative, the only solution is :\n{xone}")
        else:
            print(f'Discriminant is strictly negative, the two solutions are:\n{xone}\n{xtwo}')
    else:
        xone = round(xone, prec)
        xtwo = round(xtwo, prec)
        if xone % 1 == 0:
            xone = int(xone)
        if xtwo % 1 == 0:
            xtwo = int(xtwo)
        if xone == xtwo:
            print(f"Discriminant is strictly positive, the only solution is :\n{xone}")
        else:
            print(f'Discriminant is strictly positive, the two solutions are:\n{xone}\n{xtwo}')


def exec_simple(x):
    a = x[1]
    b = x[0]
    answer = (b * -1) / a
    print(f'The solution is:\n{answer}')
