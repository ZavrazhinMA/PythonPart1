"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def user_info(name: str,
              surname: str,
              year_of_birth: int,
              city: str,
              email: str,
              tel_number: int):
    """
    выводит данные о пользователе
    :param name:
    :param surname:
    :param year_of_birth:
    :param city:
    :param email:
    :param tel_number:
    :return:
    """
    print(f"{name} {surname}\n"
          f"Родился в {year_of_birth} году в городе {city} \n"
          f"Контактные данные: email: {email}, моб: {tel_number}")


user_info("Инокетий", "Петушинский", 1999, "Кондопога", "Kesha@etushkov.ru", 79095541212)