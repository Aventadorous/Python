class Rectangle:
    def __init__(self, color="green", width=100, height=100):
        self.color = color
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimetr(self):
        return (self.width + self.height) * 2


rect1 = Rectangle()
print("Color:", rect1.color)
print("Square:", rect1.square())
print(" ")

rect1 = Rectangle("Yellow", 23, 24)
print("Color:", rect1.color)
print("Square:", rect1.square())
print("Perimetr:", rect1.perimetr())
print(" ")

rect1 = Rectangle("Black", 10, 25)
print("Color:", rect1.color)
print("Square:", rect1.square())
print("Perimetr:", rect1.perimetr())



