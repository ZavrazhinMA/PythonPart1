"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
соответствующее сообщение. При этом работа скрипта не должна завершаться."""


class NumberErr(Exception):
    message = 'В итоговый список будут добавлены только числовые значения'


def is_num(text: str):
    """
    Подготавливает число для проверки на isdigit удаляя точки и знак минуса и лишние пробелы
    :param text:
    :return:
    """
    num_to_check = text
    if num_to_check.count('-') == 1:
        num_to_check = num_to_check[1:]
    if num_to_check.count('.') == 1:
        num_to_check = num_to_check.replace('.', '')
    if num_to_check.strip().isdigit():
        return float(text.strip())
    else:
        raise NumberErr


result_list = []
fl = 0
while fl == 0:
    list_input = input("Введите значения для проверки разделенные пробелом. 'stop' для выхода \n").split(sep=' ')
    # print(list_input)

    for el in list_input:
        if el.lower() == "stop":
            fl = 1
            break
        try:
            result_list.append(is_num(el))
        except NumberErr as ne:
            print(f"{ne.message}\n Элемент {el} не будет добавлен в итоговый список\n")
            continue


print(result_list)
