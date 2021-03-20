from random import randint
from pycat.core import Window
from pycat.keyboard import KeyCode
from pycat.label import Label
from pycat.scheduler import Scheduler
from pycat.sprite import Sprite


window = Window(enforce_window_limits=False, background_image="background.png", width=900, height=504)


class Score(Label):
    def on_create(self):
        self.score = 0

    def on_update(self, dt: float):
        self.text = "Score=" + str(int(self.score)) 


score = window.create_label(Score)


class Player(Sprite):

    def on_create(self):
        self.image = "bird.gif"
        self.y = window.center.y
        self.x = 200
        self.scale = 0.2

    def on_update(self, dt):
        self.y -= 1
        if window.is_key_down(KeyCode.SPACE):
            self.y += 30

        if self.y < 0:
            self.delete()

        if self.is_touching_window_edge():
            self.delete()
            print(score.score)
            window.close()


class Pipe(Sprite):
 
    def on_create(self):
        self.image = "pipe.png"
        self.x = window.width + self.width/2
        self.scale = 0.7
    def on_update(self, dt):
        self.x -= 8
        if self.x < -self.width/2 :
            self.delete()
            score.score += 0.5

        if self.is_touching_sprite(player):
            print(score.score)
            window.close()
    

def create_pipe(dt):
    bot_pipe = window.create_sprite(Pipe)
    top_pipe = window.create_sprite(Pipe)
    top_pipe.rotation = 180
    top_pipe.y = window.height
    y_offset = randint(-100, 100)
    top_pipe.y += y_offset
    bot_pipe.y += y_offset
    gap_offset = randint(0, 100)
    top_pipe.y += gap_offset
    bot_pipe.y -= gap_offset


Scheduler.update(create_pipe, 1.5)

player = window.create_sprite(Player)

window.run()