from pycat.base.color import Color
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window
from pycat.keyboard import KeyCode
from pycat.window import Sprite


window = Window(background_image = "Colorful City.png")
window.background_sprite.scale = 1.35
window.background_sprite.opacity = 90



class Enemy(Sprite):
    def on_create(self):
        self.x = 1000
        self.y = 200
        self.scale = 0.8
        self.image = "Frank-a.png"


class Platforms(Sprite):
    def on_create(self):
        self.scale = 0.4
        self.image = "Truck-b.png"


class Player(Sprite):
    def on_create(self):
        self.x = 200
        self.y = 230
        self.scale = 0.5
        self.image="Hare-b.png"
        self.x_speed = 0
        self.y_speed = 0
    
    def on_update(self, dt):
        self.x += self.x_speed
        self.y += self.y_speed
        self.y_speed -= 1

    def on_click_anywhere(self, mouse_event: MouseEvent):
        x_dist = mouse_event.position.x - self.x
        y_dist = mouse_event.position.y - self.y
        self.x_speed = x_dist * 0.05
        self.y_speed = y_dist * 0.05


window.create_sprite(Enemy)
window.create_sprite(Platforms, x = 200, y = 150)
window.create_sprite(Platforms, x = 450, y = 350)
window.create_sprite(Platforms, x = 700, y = 200)
window.create_sprite(Player)

window.run()