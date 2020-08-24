"""2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
элементов необходимо использовать функцию input()."""
while True:
    el_numbers_in = input('Введите количество элементов в списке ')
    try:
        el_numbers = int(el_numbers_in)
        break
    except (TypeError, ValueError) as error:
        print('Not number')
    continue
text_to_list = []
j = 1
while j <= el_numbers:
    text_to_list.append(input("введите {}-й элемнет списка и нажмите Enter ".format(j)))
    j += 1

# text_to_list = input("Введите элемнеты списка. В качестве разделителя использовать запрятую ").split(sep=",")

print(text_to_list)
i = 0
while i < len(text_to_list) - 1:
    a = text_to_list[i]
    text_to_list[i] = text_to_list[i + 1]
    text_to_list[i + 1] = a
    i += 2
print(text_to_list)
