from pycat.window import Window
from pycat.sprite import Sprite
from pycat.scheduler import Scheduler
from pycat.label import Label
import random

window=Window(background_image="underwater_04.png")

score_lable=Label("allien in spaceship=0")
window.add_label(score_lable)
score_lable.x=550
score_lable.y=600

class Spaceship(Sprite):

    def on_create(self):
        self.image="saucer.png"
        self.y=500
        self.scale=0.3
        self.score=0
        self.add_tag(Spaceship)
    def on_update(self, dt):
        self.move_forward(8)
        if self.touching_window_edge():
            self.rotation+=180
            
space_ship=window.create_sprite(Spaceship)

class Alliens(Sprite):
    def on_create(self):
        self.image = random.choice(["1.png","2.png","3.png","4.png","5.png"])
        self.scale=0.3
        self.goto_random_position()
        self.y=100
        self.is_moving_up=False
    
    def on_update(self, dt):
        if self.is_moving_up:
            self.y+=15

        if self.touching_any_sprite_with_tag(Spaceship):

            self.touching_any_sprite()
            space_ship.score+=1
            print(space_ship.score)
            self.delete()
               
            score_lable.text="allien in spaceship=" +str(space_ship.score)
            
        if self.touching_window_edge():
            self.delete()
       
    def on_left_click(self):
         self.is_moving_up=True

    def my_custom_update(dt):
        window.create_sprite(Alliens)
    Scheduler.update(my_custom_update, delay=0.5)

window.create_sprite(Alliens)

window.run()