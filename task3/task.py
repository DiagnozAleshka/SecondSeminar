""" Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму. """
n = int(input('введите N: '))
suma = 0

for i in range(1, n+1):
    suma = int(suma + round((1+1/i)**i,0))
    print(f'{i}: {suma}')
