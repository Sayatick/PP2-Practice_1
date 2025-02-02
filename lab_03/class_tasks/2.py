class Shape:
    def __init__(self):
        self.area_of_shape = 0
        
    def area(self):
        print(self.area_of_shape)

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        
    def area(self):
        print(self.length**2)

shape = Shape()
shape.area()

square = Square(5)
square.area()