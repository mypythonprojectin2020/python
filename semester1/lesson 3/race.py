from pycat.window import Window
from pycat.sprite import Sprite
from pycat.keyboard import KeyCode
w = Window()
player_has_won = False

class pig(Sprite):
    def on_create(self):
        self.image = "pig.png"
        self.y=450

    def on_update(self, dt):
        
        if self.window.get_key(KeyCode.D):
            self.x +=15
        if self.window.get_key(KeyCode.S):
            self.x -=15
        if self.window.get_key(KeyCode.E):
            self.y +=15
        if self.window.get_key(KeyCode.X):
            self.y -=15

        global player_has_won
        if self.x > w.width and not player_has_won:
            print("pig is the winner")
            player_has_won = True

class tiger(Sprite):
    def on_create(self):
        self.image = "tiger.png"
        self.y=300

    def on_update(self, dt):
        if self.window.get_key(KeyCode.H):
            self.x +=15
        if self.window.get_key(KeyCode.G):
            self.x -=15
        if self.window.get_key(KeyCode.Y):
            self.y +=15
        if self.window.get_key(KeyCode.B):
            self.y -=15

        global player_has_won
        if self.x > w.width and not player_has_won:
            print("tiger is the winner")
            player_has_won = True

class rat(Sprite):
    def on_create(self):
        self.image = "rat.png"
        self.y=150

    def on_update(self, dt):
        if self.window.get_key(KeyCode.K):
            self.x +=15
        if self.window.get_key(KeyCode.J):
            self.x -=15
        if self.window.get_key(KeyCode.I):
            self.y +=15
        if self.window.get_key(KeyCode.M):
            self.y -=15

        global player_has_won
        if self.x > w.width and not player_has_won:
            print("rat is the winner")
            player_has_won = True


w.create_sprite(pig)
w.create_sprite(tiger)
w.create_sprite(rat)



w.run()