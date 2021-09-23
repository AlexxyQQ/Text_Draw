import pygame
from tkinter import *


def gen_grid_win(ppi_choose, w_choose, h_choose):
    screen = pygame.display.set_mode((w_choose, h_choose))

    class spot:
        def __init__(self, x, y):
            self.i = x
            self.j = y
            self.f = 0
            self.g = 0
            self.h = 0
            self.neighbors = []
            self.previous = None
            self.obs = False
            self.closed = False
            self.value = 1

        def show(self, color, st):
            if self.closed == False:
                pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h),
                                 st)
                pygame.display.update()

        def path(self, color, st):
            pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
            pygame.display.update()

        def addNeighbors(self, grid):
            i = self.i
            j = self.j
            if i < ppi - 1 and grid[self.i + 1][j].obs == False:
                self.neighbors.append(grid[self.i + 1][j])
            if i > 0 and grid[self.i - 1][j].obs == False:
                self.neighbors.append(grid[self.i - 1][j])
            if j < ppi - 1 and grid[self.i][j + 1].obs == False:
                self.neighbors.append(grid[self.i][j + 1])
            if j > 0 and grid[self.i][j - 1].obs == False:
                self.neighbors.append(grid[self.i][j - 1])

    ppi = ppi_choose
    grid = [0 for i in range(ppi)]

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    grey = (220, 220, 220)
    w = w_choose / ppi
    h = h_choose / ppi

    # create 2d array
    for i in range(ppi):
        grid[i] = [0 for i in range(ppi)]

    # Create Spots
    for i in range(ppi):
        for j in range(ppi):
            grid[i][j] = spot(i, j)

    # SHOW RECT
    for i in range(ppi):
        for j in range(ppi):
            grid[i][j].show((255, 255, 255), 1)

    for i in range(0, ppi):
        grid[0][i].show(grey, 0)
        grid[0][i].obs = True
        grid[ppi - 1][i].obs = True
        grid[ppi - 1][i].show(grey, 0)
        grid[i][ppi - 1].show(grey, 0)
        grid[i][0].show(grey, 0)
        grid[i][0].obs = True
        grid[i][ppi - 1].obs = True

    pygame.init()

    def mousePress(x):
        t = x[0]
        w = x[1]
        g1 = t // (w_choose // ppi)
        g2 = w // (h_choose // ppi)
        acess = grid[g1][g2]

        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)

    loop = True
    while loop:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                    mousePress(pos)
                except:
                    pass


def start_win():
    def call_gen():
        gen_grid_win(int(ppi.get()), int(Width.get()), int(Height.get()))

    root = Tk()
    root.geometry('200x200+0+0')

    Width = StringVar()
    Height = StringVar()
    ppi = StringVar()
    Label(root, text='Width', font=('Arial', 15)).pack()
    Entry(root, text=Width, font=('Arial', 15)).pack()
    Label(root, text='Height', font=('Arial', 15)).pack()
    Entry(root, text=Height, font=('Arial', 15)).pack()
    Label(root, text='Ppi', font=('Arial', 15)).pack()
    Entry(root, text=ppi, font=('Arial', 15)).pack()

    Button(root, text='Gen', font=('Arial', 15), command=call_gen).pack()

    root.mainloop()


start_win()