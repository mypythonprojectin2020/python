from pycat.core import Window
from pycat.sprite import Sprite

window = Window()

class Turtle(Sprite):
    def on_create(self):
        self.time = 0

    def draw_triangle(self, length):
        A = t.position = window.center
        t.move_forward(length)
        B = t.position
        t.rotation += 15
        t.move_forward(length)
        C = t.position
        t.rotation += 50
        t.move_forward(length)
        D = t.position
        

        window.create_line(A.x, A.y, B.x, B.y)
        window.create_line(B.x, B.y, C.x, C.y)
        window.create_line(C.x, C.y, D.x, D.y)
        window.create_line(D.x, D.y, A.x, A.y)


    def on_update(self, dt):
        window.clear_drawables()
        self.time += 10*dt
        
        for i in range(30):
            t.draw_triangle(i*5)
            t.move_forward(20)
           
            
            

t = window.create_sprite(Turtle)

window.run()