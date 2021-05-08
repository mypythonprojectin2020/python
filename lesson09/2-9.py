from pycat.base.color import Color
from pycat.core import Window, Sprite
from random import choice
from typing import List
HEIGHT = 900
WIDTH = 500
GUESS_Y0 = 200
window = Window(width = WIDTH, height = HEIGHT)

class Choices(Sprite):
    current_color = None

    def on_create(self):
        self.x = 75
        self.y = 100
        self.scale = 50

    def on_left_click(self):
        Choices.current_color = self.color
        

color_list = [
    Color.RED,
    Color.BLUE, 
    Color.YELLOW, 
    Color.ORANGE
]

for i in range(4):
    c = window.create_sprite(Choices)
    c.x += i*(c.width + 50)
    c.color = color_list[i]


class CheckButton(Sprite):

    def on_create(self):
        self.x = 450
        self.y = 100
        self.scale = 25
        self.count_guess = 0 
        self.red_pegs = 0
        self.white_pegs = 0

    def count_pegs(self):
        self.red_pegs = 0
        self.white_pegs = 0
        maybe_white_code = []
        maybe_white_guess = []
        for i in range(4):
            if guess_list[i].color == code_list[i].color:
                self.red_pegs += 1
            else:
                maybe_white_code.append(code_list[i].color)
                maybe_white_guess.append(guess_list[i].color)

        for color in maybe_white_guess:
            if color in maybe_white_code:
                self.white_pegs += 1
                maybe_white_code.remove(color)
            print(self.red_pegs, self.white_pegs)


    def on_left_click(self):
        
        self.count_pegs()
        
        shows_pegs(self.count_guess, self.red_pegs, self.white_pegs)
        
        if self.red_pegs == 4:
            print("you win")

        if self.count_guess >= 9:
            window.close()

        else:
            self.count_guess += 1
            make_new_guess(self.count_guess)


def shows_pegs(guess, red_pegs, white_pegs):
    for i in range(red_pegs + white_pegs):
        s = window.create_sprite()
        s.x = checkbotton.x + i*13
        s.y = GUESS_Y0
        if i < red_pegs:
            s.color = Color.RED
        s.scale = 10
        s.y += guess*(c.height + 10)

def make_new_guess(guess):
    guess_list.clear()
    for i in range(4):
        c = window.create_sprite(Guess)
        c.x += i*(c.width + 50)
        c.y += guess*(c.height + 10)
        guess_list.append(c)


def check_red_pegs():
    red_pegs = 0
    for i in range(4):
        if guess_list[i].color == code_list[i].color:
            red_pegs += 1
    return red_pegs


class Guess(Sprite):

    def on_create(self):
        self.x = 75
        self.y = GUESS_Y0
        self.scale = 50

    def on_left_click(self):
        if Choices.current_color is not None:
            self.color = Choices.current_color
            
guess_list: List[Guess] = []
make_new_guess(0)

class ColorCode(Sprite):

    def on_create(self):
        self.scale = 50
        self.x = 75
        self.y = window.height - (self.height/2 + 50)
        
code_list: List[ColorCode] = []
for i in range(4):
    c = window.create_sprite(ColorCode)
    c.x += i*(c.width + 50)
    c.color = choice(color_list)
    code_list.append(c)
    
checkbotton = window.create_sprite(CheckButton)

window.run()