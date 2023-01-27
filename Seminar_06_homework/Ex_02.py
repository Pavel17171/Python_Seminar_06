# Ex_2. list comprehension, zip, enumerate

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#     Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

# Рандомное создание и заполнение скиска
list1 = [randint(1, 9) for i in range(randint(3, 10))]
print(f"Исходный список: {list1}")

# Количество пар для умножения
length = (len(list1) // 2 + 1 * (len(list1) % 2))

# Создание кортежей для вывода пар элементов на печать
list2 = zip(list1[ : length], list1[ : length - 1 - (len(list1)) % 2: -1])
list2 = list(list2)

# Создание списка результата перемножения элементов списка
list3 = []
for i in range(length):
    list3.append(list1[i] * list1[-(i + 1)])

# Вывод на печать
for i, count in enumerate(list2, start = 1):
    print(f'Пара чисел № {i} => {count} => Произведение равно: {list3[i-1]}')