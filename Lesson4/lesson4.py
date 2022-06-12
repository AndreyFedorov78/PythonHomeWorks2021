#!/usr/local/opt/python@3.10/bin/python3
import subprocess
from functools import reduce

choose = "-"
while choose != "":
    print()
    choose = input("Выберете номер задания 1-7, или enter для выхода: ")
    if choose == "1":
        print("Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта "
              "заработной платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) "
              "+ премия. Во время выполнения расчёта для конкретных значений необходимо "
              "запускать скрипт с параметрами.\n")
        subprocess.run(["./script1.py", "100", "300", "10000"])
        subprocess.run(["./script1.py", "AA0", "300", "10000"])
        subprocess.run(["./script1.py", "0"])

    elif choose == "2":
        print("Задание 2. Представлен список чисел. Необходимо вывести элементы исходного списка, "
              "значения которых больше предыдущего элемента.")


        def my_new_list(first_list):
            for index, value in enumerate(first_list[1:]):
                if value > first_list[index]:
                    yield value

        result = [x for x in my_new_list([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55])]
        print(result)

    elif choose == "3":
        print(
            "Задание 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку."
            " Подсказка: используйте функцию range() и генератор. ")
        print([x for x in range(20, 241) if 0 == x % 20 or 0 == x % 21])

    elif choose == "4":
        print("Задание 4. Представлен список чисел. "
              "Определите элементы списка, не имеющие повторений. "
              "Сформируйте итоговый массив чисел, соответствующих требованию. "
              "Элементы выведите в порядке их следования в исходном списке. "
              "Для выполнения задания обязательно используйте генератор. ")

        def my_list2(start_list):
            for index, value in enumerate(start_list):
                if not (value in start_list[0:index] or value in start_list[index + 1:]):
                    yield value
        print([x for x in my_list2([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11])])

    elif choose == "5":
        print("Задание 5. Реализовать формирование списка, используя функцию range() и возможности генератора."
              " В список должны войти чётные числа от 100 до 1000 (включая границы). "
              "Нужно получить результат вычисления произведения всех элементов списка.")
        print(reduce(lambda a, b: a*b, [x for x in range(100, 1001, 2)]))

    elif choose == "6":
        print("Задание 6.Реализовать два небольших скрипта:\n"
              "итератор, генерирующий целые числа, начиная с указанного;\n"
              "итератор, повторяющий элементы некоторого списка, определённого заранее.")

        subprocess.run(["./script6.py", "101", "30"])

    elif choose == "7":
        print("Задание 7.Реализовать генератор с помощью функции с ключевым словом yield, "
              "создающим очередное значение. При вызове функции должен создаваться объект-генератор. "
              "Функция вызывается следующим образом: for el in fact(n). "
              "Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, "
              "начиная с 1! и до n!.")

        def fact(n):
            result6 = 1
            for item in range(1, n+1):
                result6 *= item
                yield result6

        for i, v in enumerate(fact(10)):
            print(f'{i+1}!={v}')

print('Bye!')
