'''
Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
В качестве символа-разделителя используйте пробел.
'''
# some_list = [int(i) for i in input().split(' ')]
# print(max(some_list), min(some_list))

'''
Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
    1) с помощью математических формул нахождения корней квадратного уравнения
    2) с помощью дополнительных библиотек Python
'''
# a, b, c = int(input('a ')), int(input('b ')), int(input('c '))
# d = pow(b,2) - 4*a*c
# if d < 0:
#     print("корней нет")
# elif d == 0:
#     print(-b/2*a)
# else:
#     print((-b+pow(d,0.5))/2*a)
#     print((-b-pow(d,0.5))/2*a)

from sympy import *
# a, b, c = int(input('a ')), int(input('b ')), int(input('c '))
#
# x = Symbol('x')
# d = solveset(a*x**2+b*x+c,x)
# print(d)

'''
Задайте два числа. Напишите программу, которая найдёт НОК 
(наименьшее общее кратное) этих двух чисел.
'''
print(lcm(int(input()), int(input())))
