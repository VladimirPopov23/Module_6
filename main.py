# module6hard.py
# 04.11.2024 Задание "Они все так похожи"

class Figure:
    sides_count = 0

    def __init__(self, sides, color):
        self.__sides = sides  # (список сторон(целые числа)),
        self.__color = color  # (список цветов в формате RGB)
        self.filled = False  # (закрашенный, bool)

    def get_color(self):  # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, r, g, b):  # принимает параметры r, g, b
        if (1 <= r <= 255 and isinstance(r, int) and 1 <= g <= 255 and isinstance(g, int) and 1 <= b <= 255
                and isinstance(b, int)):  # проверяет корректность переданных значений перед установкой нового цвета
            return True
        else:
            return False

    def set_color(self, r, g, b):  # принимает параметры r, g, b
        if self.__is_valid_color(r, g, b):  # проверяет их на корректность
            self.__color = (r, g, b)  # и изменяет атрибут __color на соответствующие значения

    def __is_valid_sides(self, *sides):  # служебный, принимает неограниченное кол-во сторон
        for side in sides:
            if isinstance(sides, int) and side > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):  # возвращает значение/я атрибута __sides
        return self.__sides

    def __len__(self):  # возвращает периметр (сумму сторон) фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # принимает новые стороны
        if len(new_sides) != self.sides_count:  # если их значение не равно, то ничего не делать
            pass
        else:  # если равно меняем на новое значение
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1  # количество сторон
    __radius = None

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = 2 * 3.14 * sides
        self.__sides = sides

    def get_squar(self):  # возвращает площадь круга
        return (self.__sides ** 2) / (4 * 3.14)  # площадь круга - длина окружности в квадрате, разделенная на четыре Пи


class Triangle(Figure):
    sides_count = 3  # количество сторон треугольника

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self, a, b, c):  # возвращает площадь треугольника со сторонами a, b, c
        p = (a + b + c) / 2  # по теореме Герона находим полупериметр
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5  # возвращаем площадь треугольника


class Cube(Figure):
    sides_count = 12  # количество сторон куба

    def __init__(self, color, sides):
        super().__init__(color, [sides] * self.sides_count)  # 12 одинаковы сторон (передаётся 1 сторона)
        self.__sides = sides

    def get_volume(self):  # объем куба (длина стороны в степени 3)
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
