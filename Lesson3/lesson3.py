#!/usr/local/opt/python@3.10/bin/python3

choose = "-"
while choose != "":
    print()
    choose = input("Выберете номер задания 1-6, или enter для выхода: ")
    if choose == "1":
        print("Задание 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. "
              "Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.")

        def function_1(a, b, log=True):
            result_1 = type(1) == type(a) or type(1.0) == type(a)
            result_1 = not (result_1 and (type(1) == type(b) or type(1.0) == type(b)))
            if result_1:
                if log: print("\033[31m\033[1mОшибка: не верные типы аргументов. \033[0m")
                return None
            if b == 0:
                if log: print("\033[31m\033[1mОшибка: попытка деления на 0. \033[0m")
                return None
            return a / b


        print("Делим 9 на 3:", end="")
        print(function_1(9, 3.0))
        print("Делим 9 на 0:")
        print(function_1(9, 0))
        print("Делим 9 на '3':")
        print(function_1(9, '3'))
        print("Делим 9 на без логирования:", end='')
        print(function_1(9, 0, log=False))

    elif choose == "2":
        print("Задание 2.  Выполнить функцию, которая принимает несколько параметров, "
              "описывающих данные пользователя: имя, фамилия, год рождения, город проживания, "
              "email, телефон. Функция должна принимать параметры как именованные аргументы. "
              "Осуществить вывод данных о пользователе одной строкой.")


        def function_2(name, family_name, birth_year=None, city=None, e_mail=None, phone=None):
            result_2 = f"{name} {family_name} год рождения: " + (
                f"{birth_year}, " if birth_year is not None else "не указан, ")
            result_2 = result_2 + f"город проживания: " + (f"{city}, " if city is not None else "не указан, ")
            result_2 = result_2 + f"электронная почта: " + (f"{e_mail}, " if e_mail is not None else "не указана, ")
            result_2 = result_2 + f"телефон: " + (f"{phone}." if phone is not None else "не указан.")
            print(result_2)
            return


        print()
        """ пробуем вызывать функцию с разными наборами поараметров """
        function_2("Иван", "Иванов")
        function_2("Джо", "Бидон", city="Вашингтон", birth_year="1942", phone="+1-202-456-14-14",
                   e_mail="president@whitehouse.gov")
        function_2("Петр", "Батарейкин", birth_year="1990", city="RU.FidoNet", e_mail="2:5020/1.1")

    elif choose == "3":
        print("Задание 3. Реализовать функцию my_func(), которая принимает "
              "три позиционных аргумента и возвращает сумму наибольших двух аргументов. ")


        def my_func(a, b, c):
            # думаю уже все верят что я умею проверять что прилетело в функцию и тут я проверку далять не буду.
            arr = [a, b, c]
            arr.sort()
            return arr[1] + arr[2]


        print(f"my_func(1, 2, 3)={my_func(1, 2, 3)}")
        print(f"my_func(1, 3, 2)={my_func(1, 3, 2)}")
        print(f"my_func(3, 2, 1)={my_func(3, 2, 1)}")
        print(f"my_func(1, 1, 1)={my_func(1, 1, 1)}")
        print(f"my_func(1000, 200, 3000)={my_func(1000, 200, 3000)}")

    elif choose == "4":
        print("Задание 4. Программа принимает действительное положительное число x и целое отрицательное число y. "
              "Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). "
              "При решении задания нужно обойтись без встроенной функции возведения числа в степень. ")

        def function_3(x, y):
            if y >= 0: return None
            result_3 = 1
            for i in range(0, abs(y)):
                result_3 /= x
            return result_3

        print(f"10^-1={function_3(10, -1)} проверка {pow(10, -1)}")
        print(f"8^-3={function_3(8, -3)} проверка {pow(8, -3)}")
        print(f"5^-2={function_3(5, -2)} проверка {pow(5, -2)}")
        print(f"433^-23={function_3(433, -23)} проверка {pow(433, -23)}")

    elif choose == "5":
        print("Задание 5. Программа запрашивает у пользователя строку чисел, "
              "разделённых пробелом. При нажатии Enter должна выводиться сумма чисел. "
              "Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. "
              "Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме. \n"
              "Но если вместо числа вводится специальный символ, выполнение программы завершается."
              " Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму"
              " этих чисел к полученной ранее сумме и после этого завершить программу.")


        def my_sum(my_numbers):
            arr = my_numbers.split(" ")
            sum_result = 0
            for i in arr:
                try:
                    sum_result += float(i)
                except ValueError:
                    # просто игнарирую любой мусор в строке
                    pass
            return sum_result


        my_str = ''
        result = 0
        print(my_str.find("end"))
        while my_str.find("end") == -1:
            my_str = input("введите числа для суммирования, разделенные пробелом, для окончания введите 'end': ")
            result += my_sum(my_str)
            print(f"Текущий результат {result}")

    elif choose == "6":
        print("Задание 6 , 7. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв "
              "и возвращающую их же, но с прописной первой буквой. "
              "Например, print(int_func(‘text’)) -> Text.\n"
              "Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. "
              "Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, "
              "но каждое слово должно начинаться с заглавной буквы. "
              "Используйте написанную ранее функцию int_func()..")


        def int_func(word):
            element = ord(word[0])
            if ord("a") <= element <= ord("z"):
                element -= 32
            return chr(element) + word[1:len(word)]


        def caps_lock(my_string):
            arr = my_string.split(" ")
            cap_result = ""
            for i in arr:
                cap_result += int_func(i) + " "
            return cap_result

        txt = "test string My name is andrey i am 44"
        print(txt, " -> ", caps_lock(txt))

print('Bye!')
