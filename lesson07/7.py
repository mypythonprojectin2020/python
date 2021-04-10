from pycat.base.color import Color
from pycat.core import Window,Point
from math import sqrt

window = Window()

A = Point(500, 600)
B = Point(800, 110)

c = abs(A.x - B.x)
a = c/2
b = sqrt(c**2 - a**2)

C = Point((A.x+B.x)/2, A.y + b)

window.create_line(A.x, A.y, B.x, B.y, width=20, color=Color.AMBER)
window.create_line(B.x, B.y, C.x, C.y, width=20, color=Color.AZURE)
window.create_line(C.x, C.y, A.x, A.y, width=20, color=Color.GREEN)

window.run()