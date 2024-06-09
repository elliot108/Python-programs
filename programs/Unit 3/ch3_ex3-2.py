from sqlite3 import Row
from turtle import dot


def do_twice(f,v):
    f(v),
    f(v)

# def print_spam():
#     print('spam')

# do_twice(print_spam)
# def print_twice(bruce):
#     print(bruce)
#     print(bruce)

# do_twice(print_twice,'spam')

def do_four(f,v):
    do_twice(f,v),
    do_twice(f,v)

# do_four(do_twice,'spam')

def draw_grid():
    print('+'+(' -'*4 + ' +')*2)
    do_four(print,'|'+' '*9+'|'+' '*9+'|')
    print('+'+(' -'*4 + ' +')*2)
    do_four(print,'|'+' '*9+'|'+' '*9+'|')
    print('+'+(' -'*4 + ' +')*2)
# draw_grid()
# print('+', end=' ')
# print('-')
def draw_rows():
    print('+'+' -'*4, end=' ')
    print('+'+' -'*4, end=' ')
    print('+'+' -'*4, end=' ')
    print('+'+' -'*4, end=' ')
    print('+')
def draw_grid4():
    draw_rows()
    do_four(print,'|'+' '*9+'|'+' '*9+'|'+' '*9+'|'+' '*9+'|')
    draw_rows()
    do_four(print,'|'+' '*9+'|'+' '*9+'|'+' '*9+'|'+' '*9+'|')
    draw_rows()
    do_four(print,'|'+' '*9+'|'+' '*9+'|'+' '*9+'|'+' '*9+'|')
    draw_rows()
    do_four(print,'|'+' '*9+'|'+' '*9+'|'+' '*9+'|'+' '*9+'|')
    draw_rows()
draw_grid4()
# draw_rows()

