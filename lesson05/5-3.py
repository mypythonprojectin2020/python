from pycat.core import Window, Color
from pycat.sprite import Sprite

grid = [
    'ppppppp',
    'ppwpwpp',
    'ppppppp',
    'pppwppp',
    'ppppppp',
    'ppwwwpp',
    'ppppppp']

PIXEL_SIZE = 100

window = Window(width = (len(grid[0]) + 2)* PIXEL_SIZE , height = len(grid) * PIXEL_SIZE)

current_color = Color.WHITE

class Changecolor(Sprite):
    def on_create(self):
        self.scale = PIXEL_SIZE
        self.color = Color.WHITE
        self.color = current_color




class Pixel(Sprite):
    def on_create(self):
        self.scale = PIXEL_SIZE-1


color = {
    'p': Color.AMBER ,
    'w': Color.WHITE ,
    'a': Color.AMBER ,
    'b': Color.BLUE ,
    'c': Color.CHARTREUSE ,
    'd': Color.CYAN,
    'e': Color.BLACK ,
}
i = 0
for key in color:
    
    s = window.create_sprite(Changecolor)
    s.x = window.width - PIXEL_SIZE/2
    s.y = window.height - PIXEL_SIZE/2 -PIXEL_SIZE * i
    
    s.color = key[1]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        s = window.create_sprite(Pixel)
        s.x = PIXEL_SIZE/2 + PIXEL_SIZE * j
        s.y = window.height - PIXEL_SIZE/2 -PIXEL_SIZE * i
        s.color = color[grid[i][j]]


window.run()