"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
 V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
 абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property."""

from abc import ABC


class Clothes(ABC):

    def __init__(self, name: str, colour: str, size: float):
        self.name = name
        self.colour = colour
        self.size = size

    @property
    def cloth_con(self):
        return self.size * 3.3 + 3.3


class Coat(Clothes):
    def __init__(self, name, colour, size, price: float):
        self.price = price
        super().__init__(name, colour, size)

    @property
    def cloth_con(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, name, colour, size, price: float):
        self.price = price
        super().__init__(name, colour, size)

    @property
    def cloth_con(self):
        return self.size / 6.5 + 0.5


if __name__ == '__main__':
    clo1 = Clothes("T-shirt", "White", 42)
    coat1 = Coat("Demi-season coat", "Black", 144, 5200)
    cost1 = Costume("Classic costume", "Blue", 102, 4200)

    print(f'Общий расход ткани на {clo1.name}, {coat1.name}, {cost1.name} сотавил'
          f' {clo1.cloth_con + clo1.cloth_con + cost1.cloth_con :.2f} п.м.')
