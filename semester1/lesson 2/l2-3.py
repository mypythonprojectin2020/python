from pycat.window import Window
from pycat.sprite import Sprite
w = Window()

class MySprite(Sprite):
    def on_create(self):
        self.image = "pig.png"
        #self.goto_random_position()
        self.x=1

    def on_update(self,dt):
        self.x +=1
        self.y +=1

    def on_left_click(self):
        print("you clicked me")

sprite1=w.create_sprite(MySprite)
sprite1.y=300
sprite1.scale=2.3
sprite2=w.create_sprite(MySprite)
sprite2.y=60


w.run()