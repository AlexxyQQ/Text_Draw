from tkinter import *
import pygame
import sys

from pygame.draw import rect


def second_window(H, W, P):

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    WIDTH = 15
    HEIGHT = 15
    MARGIN = 1
    grid = []
    for row in range(int(W)):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(int(H)):
            grid[row].append(0)  # Append a cell

    pygame.init()
    WINDOW_SIZE = [int(W), int(H)]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    done = False

    clock = pygame.time.Clock()

    def mouse_press(pos):
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (int(W) // 15)
        row = pos[1] // (int(H) // 15)
        # Set that location to one
        print(grid[row][column])
        grid[row][column] = 1

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if pygame.mouse.get_pressed()[0]:
                try:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    mouse_press(pos)
                except:
                    pass

        screen.fill(BLACK)

        for row in range(int(W)):
            for column in range(int(H)):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                pygame.draw.rect(
                    screen,
                    color, [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

        clock.tick(60)
        pygame.display.update()
        #pygame.display.flip()

    pygame.quit()
    '''global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((int(W), int(H)))
    CLOCK = pygame.time.Clock()
    SCREEN.fill((0, 0, 0))
    a = (21, 26, 120)
    coordinates = []

    def draw():
        rect = pygame.Rect(coordinates[1])
        pygame.draw.rect(SCREEN, a, rect, 0)
        pygame.display.update()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed()[0]:
                try:
                    pos = pygame.mouse.get_pos()
                except:
                    pass

        for i in range(0, int(W), 16):
            for j in range(0, int(H), 16):
                coordinates.append((i, j))
        draw()

'''


def first_window():

    WIN = Tk()
    WIN.geometry('500x500')
    WIN.config(bg='black')
    """ Background """
    Frame_bg = PhotoImage(file='Images\Frame 1.png')
    Label(WIN, image=Frame_bg).place(x=0, y=0)
    """ Variables """
    HEIGHT = StringVar()
    HEIGHT.set('250')
    WIDTH = StringVar()
    WIDTH.set('250')
    PPI = StringVar()
    PPI.set('50')
    """ Entry Checks """
    def clear_heignt(event):
        if HEIGHT.get() == '250':
            HEIGHT.set('')

    def clear_width(event):
        if WIDTH.get() == '250':
            WIDTH.set('')

    def clear_ppi(event):
        if PPI.get() == '50':
            PPI.set('')

    def check_height_val(event):
        def check():
            try:
                if int(HEIGHT.get()) > 1000:
                    Warning.config(text='Window height too big')
                    Warning.place(x=145, y=365)
                    WIN.after(500, HEIGHT.set(''))
                else:
                    Warning.config(text='')
            except:
                Warning.config(text='Please Enter Numaric Values only')
                Warning.place(x=109, y=365)
                WIN.after(50, HEIGHT.set(''))

        WIN.after(50, check)

    def check_width_val(event):
        def check():
            try:
                if int(WIDTH.get()) > 1000:
                    Warning.config(text='Window width too big')
                    Warning.place(x=145, y=365)
                    WIN.after(500, WIDTH.set(''))
                else:
                    Warning.config(text='')
            except:
                Warning.config(text='Please Enter Numaric Values only')
                Warning.place(x=109, y=365)
                WIN.after(50, WIDTH.set(''))

        WIN.after(50, check)

    def check_ppi_val(event):
        def check():
            try:
                if int(PPI.get()) > 100:
                    Warning.place(x=180, y=365)
                    Warning.config(text='Pixels too much')
                    WIN.after(500, PPI.set(''))
                else:
                    Warning.config(text='')
            except:
                Warning.config(text='Please Enter Numaric Values only')
                Warning.place(x=109, y=365)
                WIN.after(50, PPI.set(''))

        WIN.after(50, check)

    Warning = Label(WIN, font=('Arial', 15), bg='#48BEBF')
    Warning.place(x=145, y=365)

    def gen_windows():
        second_window(HEIGHT.get(), WIDTH.get(), PPI.get())

    """ Entries """
    H = Entry(WIN,
              text=HEIGHT,
              font=('Arial', 25),
              width=4,
              bg='#42C9B5',
              fg='white',
              bd=0)
    H.place(x=166, y=150)
    H.bind('<Button-1>', clear_heignt)
    H.bind('<Key>', check_height_val)

    W = Entry(WIN,
              text=WIDTH,
              font=('Arial', 25),
              width=4,
              bg='#44C5BB',
              fg='white',
              bd=0)
    W.place(x=166, y=229)
    W.bind('<Button-1>', clear_width)
    W.bind('<Key>', check_width_val)

    P = Entry(WIN,
              text=PPI,
              font=('Arial', 25),
              width=4,
              bg='#46C1BC',
              fg='white',
              bd=0)
    P.place(x=166, y=306)
    P.bind('<Button-1>', clear_ppi)
    P.bind('<Key>', check_ppi_val)

    Button_image = PhotoImage(file='Images\Button Grn.png')
    Button(
        WIN,
        image=Button_image,
        bg='#48BEBF',
        bd=0,
        activebackground='#48BEBF',
        command=gen_windows,
    ).place(x=76, y=400)

    WIN.mainloop()


first_window()
