from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
from pycat.scheduler import Scheduler
from pycat.collision import is_aabb_collision

w=Window(background_image="img/beach_03.png")

class Player(Sprite):

    def on_create(self):
        self.image="img/cat.png"
        self.y=40
    def on_update(self, dt):
        if self.window.get_key(KeyCode.LEFT):
            self.scale_x=-1
            self.x += -3
        

        if self.window.get_key(KeyCode.RIGHT):
            self.scale_x=1
            self.x += 5
        

w.create_sprite(Player)

class Gem(Sprite):

    def on_create(self):
       self.image="img/gem_shiny01.png"
       self.goto_random_position()
       self.y=w.height
       self.scale=0.25

    def on_update(self, dt):
        self.y -= 3
        if  is_aabb_collision(self,Player):
            self.delete()
        
        if self.y<0:
            self.delete()

w.create_sprite(Gem)

def my_custom_update():
     w.create_sprite(Gem)

Scheduler.update(my_custom_update, delay=0.2)

w.run()