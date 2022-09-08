""" Реализуйте алгоритм перемешивания списка. """
from random import randint, random, shuffle


lst = [randint(-5,50) for i in range(5)]
print(lst)
shuffle(lst)
print(lst)