"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""

try:
    with open(r'D:\less4.txt', 'r', encoding="UTF-8-sig") as file_ob:  # исходил из условия что, путь к файлу задан явно
        lines = 0
        list_str = file_ob.readlines()
        print(list_str)
        if not list_str:
            print("Пустой тектовой файл. Количество строк и слов = 0")
        else:
            for en, line in enumerate(list_str, 1):
                lines += 1
                print(f"В {en}-ой строке количество слов = {len(line.split())}")
        print(f"Количество строк - {lines}")
except IOError or FileNotFoundError as er:
    print(f"Ошибка ввода вывода или файл не найден: {er}")

    #  была проблема с \ufeff (ВОМ) - применил кодировку UTF-8-sig не знаю насколько это законно