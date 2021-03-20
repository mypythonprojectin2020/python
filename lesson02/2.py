from pycat.base.base_sprite import RotationMode
from pycat.base.color import Color
from pycat.base.event.mouse_event import MouseEvent
from pycat.core import Window
from pycat.window import Sprite
from enum import Enum, auto


window = Window(background_image = "Colorful City.png")
window.background_sprite.scale = 1.35
window.background_sprite.opacity = 90


class AlienState(Enum):

    WAITING_FOR_CLICK = auto()
    MOVING = auto()
    RESETTING = auto()


class Enemy(Sprite):

    def on_create(self):
        self.x = 1000
        self.y = 200
        self.scale = 0.8
        self.image = "Frank-a.png"

    def add_hitbox(self):
        self.hitbox = window.create_sprite()
        self.hitbox.position = self.position
        self.hitbox.width = self.width * 0.65
        self.hitbox.height = self.height * 0.65
        self.hitbox.color = Color.AMBER
        self.hitbox.opacity = 0


class Platforms(Sprite):

    def on_create(self):
        self.scale = 0.4
        self.image = "Truck-b.png"
        
    def add_hitbox(self):
        self.hitbox = window.create_sprite()
        self.hitbox.position = self.position
        self.hitbox.width = self.width * 0.6
        self.hitbox.height = self.height * 0.75
        self.hitbox.color = Color.AMBER
        self.hitbox.opacity = 0

    def on_update(self, dt):
        self.x += 1
        if self.is_touching_window_edge():
            self.delete()



class Player(Sprite):


    def on_create(self):
        self.image="Hare-b.png"
        self.rotation_mode = RotationMode.RIGHT_LEFT
        self.reset()

    def reset(self):
        self.x = 200
        self.y = 230
        self.scale = 0.5
        self.rotation = 0
        self.x_speed = 0
        self.y_speed = 0
        self.state = AlienState.MOVING


    def on_update(self, dt):
        if self.state == AlienState.MOVING :
            prev_y = self.y
            self.x += self.x_speed
            self.y += self.y_speed
            self.y_speed -= 1


            for p in platform :
                
                if self.is_touching_sprite(p.hitbox):
                    top_y = p.hitbox.height/2 + self.height/2 + p.hitbox.y
                    if prev_y >= top_y :
                        self.y = top_y
                        self.state = AlienState.WAITING_FOR_CLICK
                        break


            if self.is_touching_window_edge() or self.is_touching_sprite(enemy.hitbox):
                self.state = AlienState.RESETTING

        if self.state == AlienState.RESETTING:
            self.rotation += 5
            self.scale *= 0.95
            if self.rotation > 180:
                self.reset()




    def on_click_anywhere(self, mouse_event: MouseEvent):
        if self.state == AlienState.WAITING_FOR_CLICK :
            x_dist = mouse_event.position.x - self.x
            y_dist = mouse_event.position.y - self.y
            self.x_speed = x_dist * 0.06
            self.y_speed = y_dist * 0.06
            if self.x_speed > 0:
                self.rotation = 0
            elif self.x_speed < 0:
                self.rotation = 180

            self.state = AlienState.MOVING

    
enemy = window.create_sprite(Enemy)
enemy.add_hitbox()
platform = [
    window.create_sprite(Platforms, x = 200, y = 150),
    window.create_sprite(Platforms, x = 450, y = 350),
    window.create_sprite(Platforms, x = 700, y = 200)
]

for p in platform:
    p.add_hitbox()

window.create_sprite(Player)

window.run()