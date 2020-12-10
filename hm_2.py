"""2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк."""

time_to_format = int(input('введите время в секундах '))
time_in_hours = time_to_format // 3600
time_in_min = (time_to_format - time_in_hours * 3600) // 60
time_in_sec = time_to_format - time_in_hours * 3600 - time_in_min * 60
print("Время в формате чч:мм:сс - {0:02}:{1:02}:{2:02}".format(time_in_hours, time_in_min, time_in_sec), sep='')
