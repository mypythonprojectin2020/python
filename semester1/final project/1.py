from os import umask
from re import match
from pycat.sprite import Sprite
from pycat.window import Window
import random
from pycat.core import Color, KeyCode
from typing import List


window=Window(background_image="2.jpg")
window.background_sprite.scale_to_width(window.width)

score=0
selected: 'Animal' = None
be_clicked_list: List['Animal'] = []
grid: List[List['Animal']] = []


class Animal(Sprite):
    def on_create(self):
        self.x = 0
        self.y = 300
        self.fall_y = 300
        self.i=0
        self.j=0
        self.image=random.choice(list_images)
        self.scale_to_width(80)

    def set_i_j(self, i, j):
        self.i=i
        self.j=j

    def set_position(self):
        self.x = 100 + self.j * 100
        self.y = 100 + 100 * self.i
        self.set_fall_position()

    def set_fall_position(self):
        self.fall_y = 100 + 100 * self.i

    def on_left_click(self):
    
        global be_clicked_list
        if len(be_clicked_list) < 2 and self not in be_clicked_list:
            be_clicked_list.append(self)
            self.color = Color.RED
            print("add")

    def on_update(self, dt): # fall
        if self.y>=self.fall_y:
            self.y-=5
            if self.y<self.fall_y:
                self.y=self.fall_y
        


list_images=["chick-b.png","unicorn running-b.png","rabbit-e.png","hedgehog-c.png","hen-d.png","fox-c.png"]

rows=5
cols=12

for i in range(rows):
    row = []
    for j in range(cols):
        a: Animal = window.create_sprite(Animal)
        a.set_i_j(i,j)
        a.set_position()
        row.append(a)
    grid.append(row)

def swap(a: Animal, b:Animal):

    a.i,b.i = b.i,a.i
    a.j,b.j = b.j,a.j
    grid[a.i][a.j] = a
    grid[b.i][b.j] = b
    a.set_position()
    b.set_position()

def fall(a: Animal, b:Animal):

    a.i,b.i = b.i,a.i
    a.j,b.j = b.j,a.j
    grid[a.i][a.j] = a
    grid[b.i][b.j] = b
    a.set_fall_position()
    b.set_fall_position()

def is_finished_falling():
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].fall_y < grid[i][j].y:
                return False
    return True

def is_finished_fading():
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].opacity<255:
                return False
    return True

class GameManager(Sprite) :
    WAIT_SWAP = 0
    CHECK_MATCHES = 1
    FALL_DOWN = 2
    MAKE_NEW_SPRITES = 3
    FADE_IN=4
    def on_create(self):
        self.is_visible == False
        self.state = GameManager.WAIT_SWAP
        self.score_label=window.create_label()
        self.score_label.y=window.height
        self.score_label.text="score=0"

    def on_update(self, dt): #switch
            if  self.state == GameManager.WAIT_SWAP:
                if len(be_clicked_list) == 2:
                    a = be_clicked_list[0]
                    b = be_clicked_list[1]
                    swap(a,b)
                    a.color = Color.WHITE
                    b.color = Color.WHITE
                    be_clicked_list.clear()
                    self.state = GameManager.CHECK_MATCHES

            elif self.state == GameManager.CHECK_MATCHES: #check
                matches=0
                global score
                for i in range(rows):
                    for j in range(cols):
                        k=j+1
                        current_image = grid[i][j].image
                        while k<cols and grid[i][k].image == current_image :
                            k += 1
                        if k - j >= 3:
                            while j < k:
                                if grid[i][j].opacity!=0:
                                    
                                    score += 1
                                    grid[i][j].opacity = 0 
                                j += 1
                                matches+=1
                                
                                
            
                for j in range(cols):
                    for i in range(rows):
                        k=i+1
                        current_image = grid[i][j].image              
                        while k < rows and grid[k][j].image == current_image :
                            k += 1
                        if k-i >=3:
                            while i < k:
                                if grid[i][j].opacity!=0:
                                    
                                    score += 1
                                    grid[i][j].opacity = 0 
                                i += 1
                                matches+=1
                                
                self.score_label.text="score="+str(score)

                for j in range(cols): #fall
                    k=0
                    for i in range(rows):
                        if grid[i][j].opacity != 0 :
                            fall(grid[i][j],grid[k][j])
                            k+=1
                if matches>0:
                    self.state = GameManager.FALL_DOWN
                else:
                    self.state = GameManager.WAIT_SWAP

            elif self.state == GameManager.FALL_DOWN:
                
                if is_finished_falling():
                    print("check")
                    self.state = GameManager.MAKE_NEW_SPRITES

            elif self.state == GameManager.MAKE_NEW_SPRITES: #new sprites
                for i in range(rows):
                    for j in range(cols):
                        if grid[i][j].opacity == 0 :
                            grid[i][j].delete()
                            grid[i][j] = window.create_sprite(Animal)
                            grid[i][j].set_i_j(i,j)
                            grid[i][j].set_position()
                            grid[i][j].opacity=0

                self.state = GameManager.FADE_IN

            elif self.state == GameManager.FADE_IN:
                for i in range(rows):
                    for j in range(cols):
                        if grid[i][j].opacity<255:
                            grid[i][j].opacity += 5

                if is_finished_fading():
                    self.state = GameManager.CHECK_MATCHES
                            
    
window.create_sprite(GameManager)

window.run()