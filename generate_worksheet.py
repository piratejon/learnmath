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

def chunks(_list, _size):
    '''
    <https://stackoverflow.com/a/312464/5403184> 2019-11-11
    '''
    for i in range(0, len(_list), _size):
        yield _list[i:i + _size]

def main(outfile, what, maxn, count):
    '''Generate a worksheet.'''

    fmt, func = {
        'add': ('{0}+{1}&={2}\\tab&&{3}', generate_addition_problems),
        'sub': ('{0}-{1}&={2}\\tab&&{3}', generate_subtraction_problems),
        'mul': ('{0}\\times{1}&={2}\\tab&&{3}', generate_multiplication_problems),
        'idiv': ('{0}\\div{1}&={2}\\tab&&{3}', generate_integer_division_problems),
        'rdiv': ('{0}\\div{1}&={2}rem{3}\\tab&&{4}' ,generate_division_problems),
    }[what]

    with open(outfile, 'w') as fout:
        fout.write('''
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath,multicol}

%% <https://tex.stackexchange.com/questions/198432/using-the-tab-command> 2019-11-11
\\newcommand\\tab[1][1cm]{\\hspace*{#1}}

%% <https://tex.stackexchange.com/questions/198432/using-the-tab-command> 2019-11-11
%\\flushbottom
\\begin{document}
\\setlength\\columnsep{30pt}
%\\setlength\\baselineskip{\\fill}
%\\setlength\\lineskip{\\fill}
%\\setlength\\parskip{\\fill}
\\begin{multicols}{3}
    \\noindent
''')

        all_problems = list(func(maxn, count))
        columns = list(chunks(all_problems, int(math.ceil(len(all_problems) / 3))))

        for colnum, column in enumerate(columns):
            print(column)
            fout.write('\\begin{alignat*}{3}\n')
            fmts = []
            for i, knowns in enumerate(column):
                blanks = {_ for _ in random.sample(range(len(knowns)), 1)}
                fmts.append(
                    fmt.format(*(
                        [
                            '\\rule{0.6cm}{0.15mm}'
                            if k in blanks else known
                            for k, known in enumerate(knowns)
                        ] + [knowns[_] for _ in sorted(blanks)])
                    )
                )

            fout.write('\\\\\n'.join(fmts))
            fout.write('\n\\end{alignat*}\n')
            if colnum < len(columns) - 1:
                fout.write('\\columnbreak\n')

        fout.write('''
\\end{multicols}
\\end{document}
''')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
