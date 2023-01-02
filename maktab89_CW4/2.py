class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f'area of rectangle: {self.length * self.width}')


rect = Rectangle(3, 4)
rect.area()
