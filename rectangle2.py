from rectangle import Rectangle,Сircle,Square
rect_1 = Rectangle(3,4)
rect_2 = Rectangle(5,12)
print("Прямооугольник", rect_1.get_perim())
print("Прямооугольник", rect_2.get_perim())

square_1 = Square(10)
square_2 = Square(30)
print("Квадрат", int(square_1.get_square()))
print("Квадрат", int(square_2.get_square()))

circle_1 = Сircle(50)
circle_2 = Сircle(55)
print("Круг", int(circle_1.get_circle()))
print("Круг", int(circle_2.get_circle()))

print("--------------------------------------------------------------")
figures =[rect_1, rect_2, square_1, square_2, circle_1, circle_2]
for figure in figures:
    if isinstance(figure,Square):
        print("S", figure.get_square())
    elif isinstance(figure,Rectangle):
        print("P", figure.get_perim())
else:
    print("C", int(figure.get_circle()))
