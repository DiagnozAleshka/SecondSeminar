""" Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11 """

a = input('введите число: ')
suma = 0
for i in a:
    if i != '.':
        suma += int(i)
print(suma)