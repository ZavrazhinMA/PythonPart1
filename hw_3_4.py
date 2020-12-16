"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""


def my_input_control(input_text: str, type_to_check=(int or float), sign="positive" or "negative"):
    """
    Проверка вводимых данных на корректность или принмает значение 0
    :param sign:
    :param input_text:
    :param type_to_check:
    :return:
    """

    while True:
        user_input = input(f'{input_text} или нажминте "q" для выхода\n')
        try:
            checked_input = (type_to_check(user_input))
            if sign == "positive" and checked_input < 0:
                print("Число должно быть положительное")
                continue
            if sign == "negative" and checked_input > 0:
                print("Число должно быть отрицательное")
                continue
            break
        except ValueError:
            checked_input = 0
            if user_input.lower() == 'q':
                checked_input = 0
                print('Данные не были введены')
                break
            print('Введенные данные не соответсвуют условию')
        continue
    return checked_input


def func_exp(x: int, y: int):
    result = x ** y
    return result


def func_exp2(x: int, y: int):
    ex = 0
    result = 1
    while ex < abs(y):
        result = result / x
        ex += 1
    return result


a = func_exp(
    my_input_control("Введите действительное положительное число", float, "positive"),
    my_input_control("Введите целое отрицательное число", int, "negative")
)
b = func_exp2(
    my_input_control("Введите действительное положительное число", float, "positive"),
    my_input_control("Введите целое отрицательное число", int, "negative")
)
c = pow(3, -3)  # для проверки
print("{:.3f}, {:.3f}, {:.3f}".format(a, b, c))