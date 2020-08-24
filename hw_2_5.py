"""5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми
значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

my_list = [7, 5, 3, 3, 2]
while True:
    raiting_in = input('Введите натуральное положительное число ')
    try:
        raiting = int(raiting_in)
        if raiting < 1:
            print("Введенное число аут оф рендж")
            continue
        break
    except (TypeError, ValueError) as error:
        print('Перечитай условие')
    continue
fl = 0
if my_list.count(raiting):
    my_list.insert(my_list.index(raiting) + my_list.count(raiting), raiting)
    fl = 1
else:
    for num, i in enumerate(my_list, 0):
        if raiting > i:
            my_list.insert(num, raiting)
            fl = 1
            break
if fl == 0:
    my_list.append(raiting)
print(my_list)
