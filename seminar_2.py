"""
Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
*Пример:*
- Для N = 5: 1, -3, 9, -27, 81
"""
"""
n = int(input())
string = ""
for i in range(0, n-1):
    string += str((-3) ** i) + ", "
string += str(-(-3 ** (n - 1)))
print(string)
"""
"""
Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.    
*Пример:*    
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
"""
n = int(input())
answer = "{"
for i in range (1,n):
    answer += str(i)+": "+str(3*i+1)+", "
answer += str(n)+": "+str(3*n+1)+"}"
print(answer)
"""
"""
Напишите программу, в которой пользователь будет задавать две строки, 
а программа - определять количество вхождений одной строки в другой.
"""
"""
search = input('String to search ')
long = input('String to search in ')
if len(search) > len(long):
    search, long = long, search
counter = 0
print(long.count(search))
"""

# 1. Напишите программу, которая принимает на вход число N и
# выдаёт последовательность из N членов.*Пример:*
# - Для N = 5: 1, -3, 9, -27, 81

n = int(input())
for i in range(0, n):
    print((-3)**i, end=" ")
