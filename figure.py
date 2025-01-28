class Shape:
    pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):

        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * 3.14159


class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side / 2

class Square(Rectangle):
    def __init__(self, width):

        self.width=width



def main():
    shapes = ['Rectangle', 'Circle', 'Triangle']

    for shape in shapes:
        if shape == 'Rectangle':
            width = int(input("Введите ширину прямоугольника: "))
            height = int(input("Введите высоту прямоугольника: "))
            rectangle = Rectangle(width, height)
            area = rectangle.calculate_area()
            print(f"Площадь прямоугольника: {area}")

        elif shape == 'Circle':
            radius = float(input("Введите радиус круга: "))
            circle = Circle(radius)
            area = circle.calculate_area()
            print(f"Площадь круга: {area}")




        else:
            side = int(input("Введите длину стороны треугольника: "))
            triangle = Triangle(side)
            area = triangle.calculate_area()
            print(f"Площадь треугольника: {area}")



if __name__ == "__main__":
    main()