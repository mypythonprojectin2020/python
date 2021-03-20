from pycat.core import Color, KeyCode, Sprite, Window, Scheduler
import random
window = Window()


class Player(Sprite):

    def on_create(self):
        self.color = Color.AMBER
        self.scale = 30
        self.speed = 10

    def on_update(self, dt):
        if window.get_key(KeyCode.W):
            self.y += self.speed
        if window.get_key(KeyCode.S):
            self.y -= self.speed
        if window.get_key(KeyCode.D):
            self.x += self.speed
        if window.get_key(KeyCode.A):
            self.x -= self.speed

    def on_left_click_anywhere(self):
        window.create_sprite(Bullet)



class Bullet(Sprite):

    def on_create(self):
        self.x=player.x
        self.y=player.y
        self.point_toward_mouse_cursor()
        self.scale=5
        self.speed=10
        self.color = Color.AMBER
        self.add_tag('bullet')
    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()



class Enemy(Sprite):

    def on_create(self):
        self.goto_random_position()
        self.color = Color.BLUE
        self.scale = 40
        self.speed = 3
        self.rotation=random.randint(0,360)
        self.time=0


    def on_update(self,dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_any_sprite_with_tag('bullet'):
            self.delete()
        
        self.time += dt
        if self.time > 2:
            enemy_bullet=window.create_sprite(EnemyBullet)
            enemy_bullet.position=self.position
            enemy_bullet.point_toward_sprite(player)
            self.time=0



class EnemyBullet(Sprite):

    def on_create(self):
        self.scale=5
        self.speed=5
        self.color = Color.BLUE

    def on_update(self, dt):
        self.move_forward(self.speed)
        if self.touching_window_edge():
            self.delete()
        if self.touching_sprite(player):
            self.delete()
    

player = window.create_sprite(Player)
def spawn_enemy():
    window.create_sprite(Enemy)
Scheduler.update(spawn_enemy, delay=1)

window.run()