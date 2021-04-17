from pycat.core import Window as W
from pycat.core import Sprite

from random import randint
window = W()

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
        self.windows = [
            [
            Window(x, y, 10 ,10)
            for y in range(self.y+20, self.y+self.height-20, 30)
            ]
            for x in range(self.x+10, self.x + self.width-10 ,20)
        ]
    
    def draw(self, t:Turtle):
        for col in self.windows:
            for w in col:
                w.draw(t)
        t.rotation = 0
        t.x, t.y = self.x, self.y
        t.draw_rect(self.width, self.height)

class Window:
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


for i in range(10):
    x = 50 + i*120
    b = Building(x, 30, 100, randint(200, 550))
    b.draw(t)
    

window.run()