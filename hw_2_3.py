"""3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict."""

while True:
    month_number_in = input('Введите номер месяца ')
    try:
        month_number = int(month_number_in)
        if (month_number < 1) or (month_number > 12):
            print("Введенное число аут оф рендж")
            continue
        break
    except (TypeError, ValueError) as error:
        print('Перечитай условие ')
    continue
seasons_list = ["зима", "весна", "лето", "осень"]
season_id = month_number // 3
if (season_id == 4) or (season_id < 1):
    print(seasons_list[0])
else:
    print(seasons_list[season_id])

season_dict = {
    12: "зима",
    1: "зима",
    2: "зима",
    3: "весна",
    4: "весна",
    5: "весна",
    6: "лето",
    7: "лето",
    8: "лето",
    9: "осень",
    10: "осень",
    11: "осень",
   }
print(season_dict.get(month_number))