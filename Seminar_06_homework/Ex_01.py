﻿#Ex_1. list comprehension.

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

print(sum([(1+1/n)**n for n in range(1, int(input('Введите значение: ')) + 1)]))