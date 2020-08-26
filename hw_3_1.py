"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def my_control(input_text: str, type_to_check=int or float):
    """
    Проверка вводимых данных на корректность
    :param input_text:
    :param type_to_check:
    :return:
    """

    while True:
        user_input = input(f'{input_text} или нажминте "q" для выхода\n')
        try:
            checked_input = (type_to_check(user_input))
            break
        except ValueError:
            checked_input = 0
            if user_input.lower() == 'q':
                print('Данные не были введены')
                break
            print('Введенные данные не соответсвуют условию')
        continue
    return checked_input


def func_div(a: float, b: float):
    if b != 0:
        result = a / b
        return result
    else:
        print("Ошибка! Деление на 0")


c = func_div(my_control("Введите число а", float), my_control("Введите число b", float))
print(c)
