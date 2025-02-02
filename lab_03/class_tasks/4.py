class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"current coordinates x: {self.x} and y: {self.y}")
    
    def move(self, x_1, y_1):
        self.x_1 = x_1
        self.y_1 = y_1
        print(f"new changed coordinates -> x: {self.x_1} and y: {self.y_1}")
    
    def dist(self):
        print("the distance between them: ", (self.x_1 - self.x)**2 + (self.y_1 - self.y)**2) # Euclidian formula

point = Point(2, 4)
point.show()
point.move(5, 8)
point.dist()