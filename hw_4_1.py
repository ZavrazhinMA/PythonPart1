"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

name_script, hour_prod, hour_salary, bonus = argv


def salary_func(a: float, b: float, c: float):
    """
    Расчет заработной платы сотрудника
    :param a:
    :param b:
    :param c:
    :return:
    """
    try:
        res_salary = float(a) * float(b) + float(c)
    except ValueError or TypeError as er:
        res_salary = 0
        print("Введены неверные данные -", er)
    return res_salary


print(f"Заработная плата сотрудника: {salary_func(hour_prod, hour_salary, bonus)}\n{name_script}")
#  python hw_4_1.py 100 2000 5555