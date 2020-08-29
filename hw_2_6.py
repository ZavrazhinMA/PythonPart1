"""6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е.
запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}"""
while True:
    good_num_in = input('Введите количество товаров ')
    try:
        good_num = int(good_num_in)
        break
    except (TypeError, ValueError) as error:
        print('Перечитай условие')
    continue
print(good_num)

key_id = input("Введите характеристики товара, в качестве разделителя используйте пробел ").split()

print(key_id)
good_structure = []
good_dict = {}
good_dict_list = []
i = 0
while i < good_num:
    a = []
    for el in key_id:
        a = [el, input(("Введите данные для значения '{}', {}-го товара ".format(el, i + 1)))]
        good_dict_list.append(a)
    list_to_tuple = [i + 1, dict(good_dict_list)]
    good_structure.append(tuple(list_to_tuple))
    i += 1
print("_" * 100)
print("Вывод структуры данных \n ", good_structure)

#  аналитика пошла
good_an = []
good_an_list = []
list_add_an = []
for el in key_id:
    j = 0
    good_an_list = []
    while j < good_num:
        good_an_list.append(good_structure[j][1].get(el))
        j += 1
        list_add_an = [el, good_an_list]
    good_an.append(list_add_an)
result = dict(good_an)
print("_" * 100)
print("Вывод результатов отбора \n ", result)

#  можно было добавить перевод из строки в числа
"""Добавлено после просмотра, разбора ДЗ.
По условию структура формируется запросом данных от пользователя, а в разборе она заполняется по готовому шаблону...
То ли у меня решение ближе к условию, то ли я его не понял"""