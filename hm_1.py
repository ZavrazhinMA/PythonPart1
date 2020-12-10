"""1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран."""

int_number = 1
print(int_number, type(int_number))
a = float(int_number)
print(a, type(a))
b = 0x11
c = 0o12
print(b-c)
print(b, type(b))
print(c, type(c))
float_var = float(input('введите целое число '))
print(float_var, "- целое число преобразовалось в вещественное")
line_var = input("введите произвольный набор символов ")
print(line_var, " - \t", type(line_var))
bool_var = True
print(type(bool_var))
