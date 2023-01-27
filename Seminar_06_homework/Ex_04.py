# Ex_4. enumerate

# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

number = int(input("Введите число: "))
list1 = []
for i in range(2, number + 1):
    while number % i == 0:
        list1.append(i)
        number //= i
    else:
        i += 1
print("Простые множители числа: ")

for i, count in enumerate(list1, start = 1):
    print(f'Множитель № {i} => {count}')