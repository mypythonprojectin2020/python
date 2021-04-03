from pycat.core import Window
from pycat.sprite import Sprite

grid = [
    'ppppppp',
    'ppppppp',
    'ppwwwpp',
    'ppwwwpp',
    'ppwwwpp',
    'ppppppp',
    'ppppppp']

PIXEL_SIZE = 100
TILE_SIZE = 16

window = Window(width = len(grid[0]) * PIXEL_SIZE , height = len(grid) * PIXEL_SIZE)

class Pixel(Sprite):
    def on_create(self):
        self.scale = PIXEL_SIZE / TILE_SIZE
        self.scale * 0.95


tile = {
    'p':"tiles/tile_017.png",
    'w':"tiles/tile_019.png"
}


for i in range(len(grid)):
    for j in range(len(grid[0])):
        s = window.create_sprite(Pixel)
        s.x = PIXEL_SIZE/2 + PIXEL_SIZE * j
        s.y = window.height - PIXEL_SIZE/2 -PIXEL_SIZE * i
        s.image = tile[grid[i][j]]


window.run()