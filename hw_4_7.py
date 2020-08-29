"""7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""
from math import factorial


def my_factorial(num_f: int):
    """
    вычисляет факториал числа
    :param num_f:
    :return:
    """
    result = 1
    for i in range(1, num_f + 1):
        result = result * i
        yield result


for el in my_factorial(3):
    print(el, end=' ')
print()
for k in range(1, 4):  # just для проверки
    print(factorial(k), end=' ')
"""
!!! Какое-то кривое условие. Особенно здесь: "а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!." Может просто  в цикле необходимо выводить значения с 1! и до n!
"""