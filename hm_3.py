"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

number = (input('Enter integer number (positive) '))
sum_number = int(number) + int(number + number) + int(number + number + number)
print(sum_number)

# method 2

sum_number = 0
digit_capacity = len(number)  # можно было циклом определить
print(digit_capacity)
i = 0
coefficient = 0
while i < 3:
    coefficient = coefficient + 10 ** (i * digit_capacity)
    sum_number = sum_number + int(number) * coefficient
    i += 1
print(sum_number)
