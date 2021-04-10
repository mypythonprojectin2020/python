
from pycat.core import Window, Color
from pycat.scheduler import Scheduler
from pycat.sprite import Sprite
from random import randint


class Cell(Sprite):

    def on_create(self):
        self.scale = CELL_SIZE * 0.98
        self.color = Color.WHITE

    def set_ij(self, i, j):
        self.i = i
        self.j = j

    def on_left_click(self):
        print(self.i, self.j)
        self.toggle_neighbors()
        self.check_for_win()

    def toggle_neighbors(self):
        i = self.i
        j = self.j
        if i+1 < M :
            grid[i+1][j].toggle_colors()
        if i-1 >= 0 :
            grid[i-1][j].toggle_colors()
        if j+1 < N :
            grid[i][j+1].toggle_colors()
        if j-1 >= 0 :
            grid[i][j-1].toggle_colors()

    def toggle_colors(self):
        if self.color == Color.WHITE:
             self.color = Color.RED
        else:
            self.color = Color.WHITE

    def check_for_win(self):
        for i in range(M):
            for j in range(N):
                if grid[i][j].color == Color.RED:
                    return
        print("you win")
        Scheduler.wait(2, window.close)


M = 6
N = 10
CELL_SIZE = 100


window = Window(width = CELL_SIZE*N, height = CELL_SIZE*M)


grid =[ [window.create_sprite(Cell) for j in range (N)]
        for i in range (M)
]


x0 = y0 = CELL_SIZE/2


for i in range (M):
    for j in range (N):
        grid[i][j].x = x0 + CELL_SIZE*j
        grid[i][j].y = y0 + CELL_SIZE*i
        grid[i][j].set_ij(i, j)

# for _ in range (7):
#     i = randint(0, M-1)
#     j = randint(0, N-1)
#     grid[i][j].toggle_neighbors()

toggle_count = 0

def my_costom_update(dt):
    global toggle_count
    i = randint(0, M-1)
    j = randint(0, N-1)
    grid[i][j].toggle_neighbors()
    toggle_count += 1
    if toggle_count > 7:
        Scheduler.cancel_update(my_costom_update)

Scheduler.update(my_costom_update, delay = 0.1)

window.run()