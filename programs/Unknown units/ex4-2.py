from ast import If
from re import S
from this import d
import turtle

# import math
# bob = turtle.Turtle()
# def arc():
    
#     angle=150
#     arc = 2*math.pi*50*(angle/360)
#     n = int(arc/3)+1
#     for k in range(7):
#         for i in range(n):
#             bob.fd(arc/n)
#             bob.lt(float(angle)/n)
#         bob.lt(107)
# arc()

# def arc():
    
#     angle=170
#     arc = 2*math.pi*50*(angle/360)
#     n = int(arc/3)+1
#     for k in range(10):
#         for i in range(n):
#             bob.fd(arc/n)
#             bob.lt(float(angle)/n)
#         bob.lt(85)
# arc()

# def print_n(s,n):
#     if n<=0:
#         return
#     print(s)
#     print_n(s,n-1)
# print_n('hello',5)

# def do_n(f,n):
#     if n<=0:
#         return
    
#     print(n)
#     f
#     do_n(f,n-1)

# do_n(print_n('hello',2),5)

# import time
# t = time.ctime()

# def check_fermat(a,b,c,n):
#     if a**n + b**n == c** n:
#         print("HOly smokes, Fermat was wrong")
#     else:
#         print ("NO, that doesn't work")
# # 5

# # user_input()

# def is_triangle(a,b,c):
#     if a+b>=c and a+c>=b and b+c>=a:
#         print("Yes")
#     else:
#         print("No")
# is_triangle(5,2,3)
# def user_input():
#     a = int(input("enter a\n"))
#     b = int(input("Enter b\n"))
#     c = int(input("Enter c\n"))
#     is_triangle(a,b,c)
# user_input()

import math
# word = '@'
# if word.isdigit() == 1:
#     print(word + " is a digit")
# else:
#     if word.isalpha() == 1:
#         print (word + " is a letter")
#     else:
#         print (word + " may be a symbol/puntuation mark.")

maths = True
physics = False
history = True
# if maths == False:
#     print ("Fail")
# else:
#     if physics == False:
#         print("Fail")
#     else:
#         if history == False:
#             print("Fail")
#         else:
#             print("Pass")

if maths == False or physics == False or history == False:
    print("Fail")
else:
    print("Pass")
