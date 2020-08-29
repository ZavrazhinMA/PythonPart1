"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle

my_list1 = []
my_list12 = []
iter_start = 10
iter_step = 2
iter_stop = 100
iter_list = [1, 3, 5]
iter_list_stop = 19

for i in count(iter_start, iter_step):
    my_list1.append(i)
    if i > iter_stop:
        break
print(my_list1)

j = 1
for el in cycle(iter_list):
    my_list12.append(el)
    if j > iter_list_stop:
        break
    j += 1
print(my_list12)