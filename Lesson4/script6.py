#!/usr/local/opt/python@3.10/bin/python3
"""
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
"""
from sys import argv
from itertools import count, cycle


def help_string(name):
    print(f"Спарвка: используйте: {name} 'начальное число', 'количество чисел'")


data = {}
a = b = 0  # чтоб пайчарм не ругался
script_name = ''
try:
    script_name, a, b = argv
except ValueError:
    help_string(argv[0])
    exit(0)

if not (a.isdigit and b.isdigit):
    help_string(script_name)
a = int(a)
b = int(b) + a
for val in count(a):
    if val == b:
        print("\n")
        break
    print(val, end=" ")
print("Значаниея по списку:")
b = b - a
a = [1, 2, 3, 100, 200, 300]
for val in cycle(a):
    if 0 == b:
        print("\n")
        break
    print(val, end=" ")
    b -= 1
