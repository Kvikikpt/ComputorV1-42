#!/usr/bin/env python3
import sys
from src import validation
from src import reduced
from src import exec


if len(sys.argv) == 2:
	arr = validation.validation(sys.argv[1])
	if arr is not None:
		x = reduced.sort_arr(arr)
		second = '-' if x[1] < 0 else '+'
		third = '-' if x[2] < 0 else '+'
		print(f'Reduced form: {x[0]} * X^0 {second} {x[1] if x[1] > 0 else -x[1]} * X^1 {third} {x[2] if x[2] > 0 else -x[2]} * X^2 = 0')
		if x[0] and x[1] and x[2]:
			exec.exec_square(x)