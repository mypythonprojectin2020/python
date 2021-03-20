from pycat.sprite import Sprite
from pycat.window import Window
import random
window=Window(background_image="forest_04.png",draw_sprite_rects=True)

clicked_sprite = []

class Card(Sprite):
    def on_create(self):
        self.is_visible=False
    def on_left_click(self):
        
        if len(clicked_sprite) < 2:
            self.is_visible=True
            clicked_sprite.append(self)

class Button(Sprite):
    def on_create(self):
        self.image="button.png"
        self.x=500
        self.y=150
        self.scale=0.3
    def on_left_click(self):
        sprite1:Sprite=clicked_sprite[0]
        sprite2:Sprite=clicked_sprite[1]
        
        if len(clicked_sprite) == 2:
            if sprite1.image == sprite2.image:
                sprite1.delete()
                sprite2.delete()
            else :
                sprite1.is_visible=False
                sprite2.is_visible=False
        clicked_sprite.clear()

avatar_list=["avatar_01.png","avatar_02.png","avatar_03.png","avatar_04.png"]*4
random.shuffle(avatar_list)
print(avatar_list)

window.create_sprite(Card,x=100,y=100,image=avatar_list.pop())
window.create_sprite(Card,x=100,y=200,image=avatar_list.pop())
window.create_sprite(Card,x=100,y=300,image=avatar_list.pop())
window.create_sprite(Card,x=100,y=400,image=avatar_list.pop())
window.create_sprite(Card,x=200,y=400,image=avatar_list.pop())
window.create_sprite(Card,x=200,y=100,image=avatar_list.pop())
window.create_sprite(Card,x=200,y=200,image=avatar_list.pop())
window.create_sprite(Card,x=200,y=300,image=avatar_list.pop())
window.create_sprite(Card,x=300,y=100,image=avatar_list.pop())
window.create_sprite(Card,x=300,y=200,image=avatar_list.pop())
window.create_sprite(Card,x=300,y=300,image=avatar_list.pop())
window.create_sprite(Card,x=300,y=400,image=avatar_list.pop())
window.create_sprite(Card,x=400,y=400,image=avatar_list.pop())
window.create_sprite(Card,x=400,y=100,image=avatar_list.pop())
window.create_sprite(Card,x=400,y=200,image=avatar_list.pop())
window.create_sprite(Card,x=400,y=300,image=avatar_list.pop())

print(avatar_list)

window.create_sprite(Button)
window.run()