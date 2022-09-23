'''
Задача HARD SORT.
Задайте двумерный массив из целых чисел. Количество строк и столбцов
задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.
Например, задан массив:
1 4 7 2
5 9 10 3
После сортировки
1 2 3 4
5 7 9 10
'''

# import random as r
#
#
# def sort(arr):
#     for k in range(len(arr)):
#         min = k
#         for i in range(k, len(arr)):
#             if arr[i] < arr[min]:
#                 min = i
#         arr[min], arr[k] = arr[k], arr[min]
#
#     return arr
#
#
# def median(arr):
#     return arr[(len(arr)) // 2]
#
#
# rows = int(input('Число строк в массиве '))
# column = int(input('Число колонок в массиве '))
# matrix = [[r.randint(-10, 10) for i in range(column)] for j in range(rows)]
# temp = []
#
#
# def print_dimentional(matrix):
#     for lists in matrix:
#         print(lists)
#     print()
#
#
# for i in range(rows):
#     for j in range(column):
#         temp.append(matrix[i][j])
#
# sorted_temp = sort(temp)
#
# print()
# print(f'median {median(sorted_temp)}')
#
# print_dimentional(matrix)
#
# for i in range(rows):
#     for j in range(column):
#         matrix[i][j] = sorted_temp[i * column + j]
#
# print_dimentional(matrix)

'''
 HARD необязательная. Сгенерировать массив случайных целых чисел размерностью 
 m*n (размерность вводим с клавиатуры). Вывести на экран красивенько таблицей. 
 Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно 
 один раз переместился на другое место и потом не участвовал никак (возможно для 
 этого удобно будет использование множества) и выполнить это за m*n / 2 итераций. 
 То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее 
 в конце опять вывести на экран как таблицу.
'''
# from random import randint
# from random import choice
#
# n = int(input("Insert n: "))
# m = int(input("Insert m: "))
#
# initList = []
# tempList = []
#
# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(randint(-10, 10))
#         tempList.append(sp[j])
#     initList.append(sp)
# print(initList)
# print(tempList)
# indexList = [0] * m*n
# for i in range(m*n):
#     indexList[i] = i
#
# for i in range(int(m*n/2)):
#     a = choice(indexList)
#     indexList.remove(a)
#     b = choice(indexList)
#     indexList.remove(b)
#     tempList[a], tempList[b] = tempList[b], tempList[a]
# resultList = []
# print(tempList)
# for i in range(n):
#     sp = []
#     for j in range(m):
#         sp.append(tempList[0])
#         tempList.remove(tempList[0])
#     resultList.append(sp)
#
# print(resultList)

'''
Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.     
    *Пример:* 
    2+2 => 4; 
    1+2*3 => 7; 
    1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
        *Пример:*         
        1+2*3 => 7; 
        (1+2)*3 => 9;
        9*(0+(4-2.5)/(3-2));
'''
def replacing_operations(op, total, exmp):
    exmp.pop(exmp.index(op) - 1)
    exmp.pop(exmp.index(op) + 1)
    exmp[exmp.index(op)] = total
    return exmp
def operations(expr):
    if '*' in expr:
        if '/' in expr:
            if expr.index('/') < expr.index('*'):
                total = expr[expr.index('/') - 1] / expr[expr.index('/') + 1]
                expr = replacing_operations('/', total, expr)
        else:
            total = expr[expr.index('*') - 1] * expr[expr.index('*') + 1]
            expr = replacing_operations('*', total, expr)
    elif '/' in expr:
        total = expr[expr.index('/') - 1] / expr[expr.index('/') + 1]
        expr = replacing_operations('/', total, expr)
    elif '+' in expr:
        if '-' in expr:
            if expr.index('-') < expr.index('+'):
                total = expr[expr.index('-') - 1] - expr[expr.index('-') + 1]
                expr = replacing_operations('-', total, expr)
        else:
            total = expr[expr.index('+') - 1] + expr[expr.index('+') + 1]
            expr = replacing_operations('+', total, expr)
    elif '-' in expr:
        total = expr[expr.index('-') - 1] - expr[expr.index('-') + 1]
        expr = replacing_operations('-', total, expr)
    return expr
def first_open(expa):
    first_op = len(expa)
    for i in range(first_op - 1, -1, -1):
        if expa[i] == '(':
            first_op = i
            break
    return first_op

def first_close(expa, first_op):
    first_cl = len(expa)
    for i in range(first_op, first_cl):
        if expa[i] == ')':
            first_cl = i
            break
    return first_cl

import re

string = input('Enter an example: ')
exp = re.findall(r'\d+\.?\d+?|[\*\-\/\+]?|\d+|\(?\)?', string)
exp = [i for i in exp if i not in '']
for i in range(len(exp)):
    if '.' in exp[i]:
        exp[i] = float(exp[i])
    elif exp[i].isdigit():
        exp[i] = int(exp[i])
while len(exp) > 1:
    if '(' in exp:
        prior = []
        for i in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
            prior.append(exp[i])
        for i in range(len(prior)):
            for j in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
                if exp[j] == prior[i]:
                    exp.pop(j)
        while len(prior) > 1:
            prior = operations(prior)

        exp.pop(first_close(exp, first_open(exp)))
        exp[first_open(exp)] = prior[0]
    else:
        exp = operations(exp)

print(exp[0])

'''
Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
*Пример:* 
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
# a = [int(s) for s in input("введите список: ").split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')

