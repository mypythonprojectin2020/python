from pycat.core import Window, Color
from pycat.sprite import Sprite
import random

window = Window()

my_list = []

for i in range(20):
    my_list.append([random.randint(0,100) for j in range(40)])
 
min_v = max_v = my_list[0][0]

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        v = my_list[i][j]
        if v < min_v:
            min_v = v
        if v > max_v:
            max_v = v


class Cell (Sprite):
    def on_create(self):
        self.width = 20
        self.height = 20

    def make_label (self, value, min, max):
        label = window.create_label()
        label.text = str(my_list[i][j])
        label.color = Color.BLUE
        label.x = self.x
        label.y = self.y
        label.font_size = 10
        scale = (value-min)/(max-min)
        c = 255 * scale
        self.color = Color(255,255-c,255-c)


for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        cell = window.create_sprite(Cell)
        cell.x = 100 + j*cell.width
        cell.y = 600 - i*cell.height
        cell.make_label(my_list[i][j],min_v,max_v)


window.run()