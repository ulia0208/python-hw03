# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import math
from random import randint

N=int(input('Введите число элементов '))

my_list=[]
for i in range(N):
    my_list.append(randint(0,10))
print(*my_list)

x=int(input('Введите искомое число '))

my_list2=[]
my_list3=[]
for i in range(len(my_list)):
    my_list2.append(my_list[i]-x)
    my_list3.append(abs(my_list[i]-x))
print(*my_list2)
print(*my_list3)

min=my_list3[0]
for i in range(len(my_list3)):

    if min>=my_list3[i]:
        min=my_list3[i]

    print(f'min {min}') 
print(min)      

for i in range(len(my_list3)):
    if min==my_list3[i]:
        print(f'{i}-й элемент массива')


