from pycat.core import Window, Sprite
from random import randint
window = Window()

class Turtle(Sprite):
    def on_create(self):
        self.position = window.center

    def draw_forward(self, distance):
        x1 = self.x
        y1 = self.y
        self.move_forward(distance)
        x2 = self.x
        y2 = self.y
        window.create_line(x1, y1, x2, y2)

    def draw_rect(self, width, height):
        for _ in range(2):
            self.draw_forward(width)
            self.rotation += 90
            self.draw_forward(height)
            self.rotation += 90

class Building:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, t:Turtle):
        t.rotation = 0
        t.x, t.y = self.x, self.y
        t.draw_rect(self.width, self.height)

t = window.create_sprite(Turtle)
for _ in range(10):

    b = Building(randint(0, 1000), randint(0, 200), randint(50,300), randint(50,300))
    b.draw(t)


window.run()