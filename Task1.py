# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random
my_list = [random.randint(0, 50) for _ in range(10)]
print(my_list)

number = int(input("Введите число Х: "))
count = 0
min_number = 0
max_number = 0


for i in range(len(my_list)):
    if number == my_list[i]:
        count += 1
## как реализовать нахождение ближайшего числа так до конца и не разобрался, в гугле в подобных задачах
## используют методы, до которых я бы сам никогда не додумался

        
           
           
        
             


    
    