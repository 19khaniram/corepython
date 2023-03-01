class shape:
    def __init__(self, c, b):
        self.colour = c
        self.borderWidth = b


class rectangle(shape):
    def __init__(self, length, width, c="", b=0):
        self.length = length
        self.width = width
        super(rectangle, self).__init__(c,b)
    def area(self):
        return self.length * self.width
    def parimeter(self):
        return 2 * self.length + 2 * self.width




class circle(shape):
    def __init__(self, r, c="", b=0):
        self.radius = r
        super(circle, self).__init__(c,b)
    def area(self):
        return self.radius * self.radius * 3.14

class triangle(shape):
    def __init__(self, h, a, c="", b=0):
        self.height = h
        self.base = a
        super(triangle, self).__init__(c,b)
    def area(self):
        return self.height * self.base * 0.5

