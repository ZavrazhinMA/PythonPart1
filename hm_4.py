"""4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

number_to_max = int(input("Enter positive integer number "))

max_result = abs(number_to_max - (number_to_max // 10) * 10)
number_to_max = number_to_max // 10
# print(abs(number_to_max // 10 - (number_to_max // 10 // 10) * 10))
while number_to_max // 10:
    if abs(number_to_max - (number_to_max // 10) * 10) > max_result:
        max_result = abs(number_to_max - (number_to_max // 10) * 10)
    number_to_max = number_to_max // 10
print(max_result)