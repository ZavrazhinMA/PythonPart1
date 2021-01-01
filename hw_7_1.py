"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д."""


# import random


class Matrix:
    def __init__(self, mat_list: list):
        self.mat_list = mat_list

    def __getitem__(self, item):
        return self.mat_list[item]

    def __str__(self):
        list_to_print = self.mat_list
        list_width = []
        k = 0

        while True:  # Идем по столбцам и ищем самое толстое число в столбце
            try:
                max_len = 0
                for i in list_to_print:
                    if len(str(i[k])) > max_len:
                        max_len = len(str(i[k]))
                list_width.append(max_len + 1)
            except IndexError:
                break
            k += 1

        #  print(list_width)
        mat_in_text = ''
        for line in list_to_print:
            for num, el in enumerate(line):
                mat_in_text += f'{el: ^{list_width[num]}}'  # центрируем текст по формату широкого числа в столбце
            mat_in_text += '\n'
        return mat_in_text

    def __add__(self, other):
        new_mat_list = []
        for num, _ in enumerate(self.mat_list):
            new_mat_list.append([a + b for a, b in zip(self[num], other[num])])
        return Matrix(new_mat_list)


if __name__ == '__main__':
    mat1 = Matrix([[1, 222, 23],
                   [111211, 333333, 555457],
                   [774, 1234, 0]])

    mat2 = Matrix([[11, 52, 23],
                   [101, 100, 57],
                   [7444544, 255444, 245223]])
    mat_sum = mat1 + mat2

    print(mat1)
    print(mat2)
    print(mat_sum)
