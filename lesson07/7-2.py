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
        t.rotation += 72
        t.move_forward(length)
        C = t.position
        t.rotation += 72
        t.move_forward(length)
        D = t.position
        t.rotation += 72
        t.move_forward(length)
        E = t.position

        window.create_line(A.x, A.y, B.x, B.y)
        window.create_line(B.x, B.y, C.x, C.y)
        window.create_line(C.x, C.y, D.x, D.y)
        window.create_line(D.x, D.y, E.x, E.y)
        window.create_line(E.x, E.y, A.x, A.y)


    def on_update(self, dt):
        window.clear_drawables()
        self.time += 10*dt
        self.rotation += self.time
        for i in range(30):
            t.draw_triangle(i*5)
            t.move_forward(20)
            t.rotation += 0.1
            
            

t = window.create_sprite(Turtle)

window.run()