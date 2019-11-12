#!/usr/bin/python3

'''
Generate worksheets to drill on math.
'''

import random
import math
import sys

def generate_addition_problems(maxn=20, count=20):
    '''
    Generate addition problems.
    '''

    for _ in range(count):
        a = random.randint(0, maxn)
        b = random.randint(0, maxn)
        yield (a, b, a + b)

def generate_subtraction_problems(maxn=20, count=20, allow_negative=False):
    '''Generate some subtraction problems.'''

    for _ in range(count):
        a = random.randint(0, maxn)
        b = random.randint(0, maxn)
        yield (a + b, a, b)

def generate_multiplication_problems(maxn=12, count=20):
    '''Generate some multiplication problems.'''

    for _ in range(count):
        a = random.randint(0, maxn)
        b = random.randint(0, maxn)
        yield (a, b, a * b)

def generate_integer_division_problems(maxn=12, count=20):
    '''Generate some multiplication problems.'''

    for _ in range(count):
        a = random.randint(0, maxn)
        b = random.randint(1, maxn)
        yield (a * b, a, b)

def generate_division_problems(maxn=200, count=20):
    '''Generate some multiplication problems.'''

    for _ in range(count):
        a = random.randint(0, maxn)
        b = random.randint(1, int(math.ceil(math.sqrt(maxn))))
        yield (a, b, a // b, a % b)

def main(what, maxn, count):
    '''Generate a worksheet.'''

    func = {
        '+': generate_addition_problems,
        '-': generate_subtraction_problems,
        '*': generate_multiplication_problems,
        '//': generate_integer_division_problems,
        '/': generate_division_problems,
    }[what]

    for p in func(maxn, count):
        blank = random.randint(0, len(p) - 1)
        p = list(p)
        print(p, blank)

if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
