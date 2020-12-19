"""Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""

from random import randrange
item_num = 10
random_list = [randrange(-85, 100) for i in range(item_num)]
list_format = [random_list[i] for i in range(item_num) if random_list[i] > random_list[i-1]]
print(random_list)
print(list_format)
#  вопрос с чем сравнивать 0-й элемент: с -1м или с нулем или из условия, что первый элемент должен быть всегда
#  list_format = [random_list[i] for i in range(item_num) if random_list[i] > random_list[i-1] or i == 0]