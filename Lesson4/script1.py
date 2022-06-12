#!/usr/local/opt/python@3.10/bin/python3
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv


def help_string(script_name):
    print(f"Спарвка: используйте: {script_name} 'выработка в часах', 'ставка в час','премия'")


data = {}
try:
    script_name, data['hours'], data['salary'], data['bonus'] = argv
except ValueError:
    help_string(argv[0])
    exit(0)

for i in data.keys():
    try:
        data[i] = float(data[i])
    except ValueError:
        help_string(script_name)
        exit(0)
print(f"в этом месяце заработано { (data['hours'] * data['salary'] + data['bonus']):,.2f} руб.".replace(","," "));
