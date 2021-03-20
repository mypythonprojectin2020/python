from re import S
from pycat.core import Sprite, Window
import random

window = Window()

class Particle(Sprite):

    def on_create(self):
        self.add_tag('particle')
        self.goto_random_position()
        self.rotation = random.randint(0, 360)
        self.scale = 5
    def on_update(self, dt):
        self.move_forward(5)   
        if self.touching_window_edge():
            self.rotation+=180

class CreateButton(Sprite):

    def on_left_click(self):
        # for particle in window.get_sprites_with_tag('particle'):
        #     pass
        for _ in range(10):
            window.create_sprite(Particle)

# class ExplodeButton(Sprite):

#     def on_left_click(self):
#         for q in range(0,360,20):
#             for particle in window.get_sprites_with_tag('particle'):
#                 q=window.create_sprite(ExplosionParticle)
#                 q.position=particle.position
                
#                 particle.delete()
            
class ExplodeButton(Sprite):

    def on_left_click(self):
        p_list=window.get_sprites_with_tag('particle')
        for p in p_list:
            for r in range(0,360,20):
                q=window.create_sprite(ExplosionParticle)
                q.position=p.position
                q.rotation=r
                p.delete()
            

class ExplosionParticle(Sprite):

    def on_create(self):
        self.rotation = random.randint(0, 360)
        self.scale=5
        self.time = 0
    def on_update(self, dt):
        self.time+= dt
        self.opacity*=0.95
        self.move_forward(5)
        if self.touching_window_edge():
            self.delete()


window.create_sprite(CreateButton,x=100,y=100,scale=50,color=(255,0,0))
window.create_sprite(ExplodeButton,x=100,y=200,scale=50,color=(0,255,0))
window.run()