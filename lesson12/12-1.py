from enum import Enum
from random import randint, choice
from pycat.base.color import Color
from pycat.core import Window, Sprite, Scheduler
from os import path
from pycat.label import Label
from get_data import get_data, write_data


folder = path.dirname(__file__)
fruit_file = folder + "/fruit.txt"
dance_file = folder + "/dance.txt"
animal_file = folder + "/animal.txt"


fruits = get_data(fruit_file)
dance = get_data(dance_file)
animals = get_data(animal_file)
words = animals + fruits + dance

class States (Enum):
    ANIMALS = 0
    FRUITS = 1
    DANCE = 2

state_list = [States.ANIMALS, States.FRUITS, States.DANCE]
current_state = choice(state_list)
print(current_state)
def change_states(dt):
    global current_state
    current_state = choice(state_list)
    print(current_state)

Scheduler.update(change_states, delay=5)

window = Window(enforce_window_limits=False)

class Score(Label):

    def on_create(self):
        self.x = window.width/2 - 10
        self.file = path.dirname(__file__)+'/highscore.txt'
        self.current = 0
        self.high = int(get_data(self.file)[0])
        self.text = "Highscore:" + str(self.high)

    def check_score(self):
        if self.current > self.high:
            self.high = self.current
            self.text = "Highscore:" + str(self.high)
            write_data(self.file, str(self.current))

score = window.create_label(Score)

class Word (Sprite):

    def on_create(self):
        self.label = window.create_label()
        self.label.font_size = 30
        self.label.color = Color.random_rgb()
        
    def set_position(self, text, x, y):
        self.label.text = text
        self.width = self.label.content_width
        self.height = self.label.content_height
        self.label.x = x
        self.label.y = y
        self.x = x + self.width/2
        self.y = y - self.height/2
    
    def on_update(self, dt):

        speed = 3
        self.y -= speed
        self.label.y -= speed
        if self.y < 0:
            self.delete()
            self.label.delete()
        

    def add_point(self):
        self.delete()
        self.label.delete()
        print("add point")
        score.current +=1
        score.check_score()
        

    def on_left_click(self):
    
        if current_state == States.DANCE and self.label.text in dance:
            self.add_point()
        elif current_state == States.FRUITS and self.label.text in fruits:
            self.add_point()
        elif current_state == States.ANIMALS and self.label.text in animals:
            self.add_point()

        else:
            print("lose point")

        
def create_word(dt):
    word = window.create_sprite(Word)
    word.set_position(choice(words), randint(0, window.width-20), window.height)

Scheduler.update(create_word, delay=0.4)
window.run()