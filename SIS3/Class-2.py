class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.l = l

    def area(self):
        return self.l * self.l


aSquare = Square(3)
print(aSquare.area())