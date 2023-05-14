class Rectangle:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def get_perim(self):
        return 2*(self.a+self.b)
class Square:
    def __init__(self, a=0):
        self.a = a
    def get_square(self):
        return self.a ** 2
class Сircle:
    def __init__(self, r=0):
        self.r = r
    def get_circle(self):
        return (3.14*(self.r)) ** 2