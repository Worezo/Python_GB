'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)'''

import random

n = int(input('Введите количество элементов массива: '))
list1 = [random.randint(-10, 10) for i in range(n)]
print(list1)

'''Вариант 1: Поиск наименьшего и наибольшего элемента в массиве
min = list1[0] if list1 else 'None'
for i in list1:
    if i < min:
        min = i
print(min)

max = list1[0] if list1 else 'None'
for i in list1:
    if i > max:
        max = i
print(max)'''

'''Вариант 2: Наибольший и наименьший вводятся вручную'''
min = int(input('Задайте минимальное значение в массиве: '))
max = int(input('Задайте максимальное значение в массиве: '))

for i in range(len(list1)):
    if min <= list1[i] <= max:
        print(i, end = ' ')

