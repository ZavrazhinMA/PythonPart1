"""4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове."""

str_to_list = input(" Введите список элеметов списка, разделенных пробелом ").split(" ")
print(str_to_list)
for num, i in enumerate(str_to_list, 1):
    print(num, " - ", i[:10])
