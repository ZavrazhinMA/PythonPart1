"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""

from random import randrange as rr

item_num = 20  # количество элемнетов в списке
random_list = [rr(-15, 20) for i in range(item_num)]
list_format = [random_list[i] for i in range(item_num) if random_list.count(random_list[i]) == 1]
print(random_list, list_format, sep='\n')