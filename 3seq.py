"""Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4"""

# 1 список

message = "Введите число "
some_element = int(input("Введите количество элементов первого списка:"))
number = 0
list_number = []

for i in range(some_element):
    number += 1
    i = message + str(number) + ':'
    print(i)
    some_number = int(input())
    list_number.append(some_number)

print(list_number)

# 2й список
message2 = "Введите число "
some_element2 = int(input("Введите количество элементов второго списка:"))
number2 = 0
list_number2 = []

for i in range(some_element2):
    number2 += 1
    i = message + str(number2) + ':'
    print(i)
    some_number2 = int(input())
    list_number2.append(some_number2)

final_list = list(set(list_number + list_number2)) #обьединяем списки, убираем повторяющиеся элементы и приводим к списку
print(final_list)

print(type(final_list))