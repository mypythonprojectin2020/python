from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode

window = Window(background_image="forest_background.jpg")

class Player(Sprite):
    def on_create(self):
        self.image = "pig.png"
        self.y=0
        self.health=50

    def on_update(self, dt):
        self.move_forward(15)
        if self.window.get_key(KeyCode.DOWN):
            self.rotation=270
        elif self.window.get_key(KeyCode.UP):
            self.rotation=90
        elif self.window.get_key(KeyCode.LEFT):
            self.rotation=180
        elif self.window.get_key(KeyCode.RIGHT):
            self.rotation=0

        if self.touching_any_sprite() or self.x>window.width:
            self.health-=1
            print(self.health)
        if self.health<0:
            print("dead")
            window.exit()
a=window.create_sprite(Player)

class Enemy(Sprite):
    def on_create(self):
        self.image = "rooster.png"
        self.y=200

    def on_update(self, dt):
        self.move_forward(2) 
        self.point_toward_sprite(a)

for x in range(0,window.width,380):
    t=window.create_sprite()
    t.image="fireball.gif"
    t.x=x
    t.y=300

s=window.create_sprite()
s.image="fireball.gif"
s.x=600
s.y=400


window.create_sprite(Enemy)

window.run()