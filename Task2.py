# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

number  = int(input("Введите количество элементов: "))
my_list = [random.randint(1, 20) for _ in range(number)]
x_number = int(input("Введите число, к которому ищем самое близкое число: "))
result_number = 0
eps = x_number

for i in my_list:
    if abs(i - x_number) < eps:
        eps = abs(i - x_number)
        result_number = i

print(my_list)
print(result_number)