"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def my_func(a: float, b: float, c: float):
    """
    сумма двух максимальных из трех чисел
    :param a:
    :param b:
    :param c:
    :return:
    """
    my_list = [a, b, c]
    min_in_list = a
    for el in my_list:
        if el < min_in_list:
            min_in_list = el
    my_list[my_list.index(min_in_list)] = 0
    result = sum(my_list)
    #  result = a + b + c - min
    #  result = sum(my_list) - min
    #  result = sum(my_list) - min(my_list)
    return result


print(my_func(3, -5, -1))
