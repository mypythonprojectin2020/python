from pycat.core import Sprite, Window
import random
window = Window()

class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 5


    def on_update(self, dt):
        self.move_forward(5)
        if self.x >= window.width:
            self.rotation += 180
        if self.x <= 0:
            self.rotation += 180
        if self.y <= 0:
             self.rotation += 180
        if self.y >= window.height:
             self.rotation += 180

for _ in range(100):
    window.create_sprite(Particle)

class ColorButton(Sprite):

    def on_left_click(self):
        for particle in window.get_sprites_with_tag('particle'):
            particle.color = self.color

window.create_sprite(ColorButton,x=100,y=100,scale=50,color=(200,0,255))
window.create_sprite(ColorButton,x=200,y=100,scale=50,color=(0,255,150))
window.create_sprite(ColorButton,x=300,y=100,scale=50,color=(0,0,255))
window.run()