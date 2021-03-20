from pycat.sprite import Sprite
from pycat.window import Window
import random
from pycat.core import Player, AudioLoop

window=Window(background_image="forest_04.png",draw_sprite_rects=True)

select_sprite_sound = Player('hit.wav')
match_sprite_sound = Player('point.wav')
no_match_sprite_sound = Player('laugh.wav')
audio_loop = AudioLoop('LoopLivi.wav', volume=0.2)

audio_loop.play()

clicked_sprite = []
left_sprite = []
class win(Sprite):
    def on_create(self):
        self.is_visible=False
        self.image=("win.png")
        self.x=600
        self.y=300
    def on_update(self, dt):
        if len(left_sprite)==8:
            self.is_visible=True
            self.rotation+=2

class Card(Sprite):
    def on_create(self):
        self.is_visible=False
        self.is_rotating=False

    def on_left_click(self):
        if len(clicked_sprite) < 2:
            select_sprite_sound.play()
            self.is_visible=True
            clicked_sprite.append(self)
    
    def on_update(self, dt):
        if self.is_rotating:
            self.rotation +=3
            self.scale -=0.01
            if self.rotation>180:
                self.delete()
                left_sprite.append(1)

                if len(left_sprite)==8:
                    window.create_sprite(win)

class Button(Sprite):
    def on_create(self):
        self.image="button.png"
        self.x=600
        self.y=200
        self.scale=0.4

    def on_left_click(self):
        sprite1:Sprite=clicked_sprite[0]
        sprite2:Sprite=clicked_sprite[1]
        
        if len(clicked_sprite) == 2:
            if sprite1.image == sprite2.image:
                sprite1.is_rotating = True
                sprite2.is_rotating = True
                match_sprite_sound.play()
            else :
                sprite1.is_visible=False
                sprite2.is_visible=False
                no_match_sprite_sound.play()

            clicked_sprite.clear()

    def on_update(self, dt):
        if len(left_sprite) == 8:
            self.delete()


avatar_list=["avatar_01.png","avatar_02.png","avatar_03.png","avatar_04.png"]*2
random.shuffle(avatar_list)
print(avatar_list)
for x in range(100,500,100):
    for y in range(100,300,100):
        window.create_sprite(Card,x=x,y=y,image=avatar_list.pop())


window.create_sprite(Button)

window.run()