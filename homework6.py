# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# n = int(input('Введите первый элемент: '))
# a = int(input('Введите разность: '))
# b = int(input('Введите количество элементов: '))

# def prog(n, a, b):
#     lst = []
#     for i in range(b):
#         lst.append(n + i * a)
#     return lst

# print(prog(n, a, b))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min = int(input('Введите минимальное число: '))
# max = int(input('Введите максимальное число: '))

# def indlst(lst, min, max):
#     lst2 = []
#     for i in range(len(lst)):
#         if min < lst[i] < max:
#             lst2.append(i)
#     return lst2

# print(indlst(lst1, min, max))