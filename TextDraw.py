#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from tkinter import *
import pygame


def second_window(Hs, Ws):

    H = int(Hs)
    W = int(Ws)

    # Define some colors

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # This sets the WIDTH and HEIGHT of each grid location

    WIDTH_rect = 15
    HEIGHT_rect = 15

    # This sets the margin between each cell

    MARGIN = 1

    Hp = H // HEIGHT_rect
    Wp = W // WIDTH_rect

    # Create a 2 dimensional array. A two dimensional
    # array is simply a list of lists.

    grid = []
    for row in range(Wp):

        # Add an empty array that will hold each cell
        # in this row

        grid.append([])
        for column in range(Hp):
            grid[row].append(0)  # Append a cell

    # Initialize pygame

    pygame.init()

    # Set the HEIGHT_rect and WIDTH_rect of the screen

    WINDOW_SIZE = [H, W]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen

    pygame.display.set_caption('Array Backed Grid')

    # Loop until the user clicks the close button.

    done = False

    # Used to manage how fast the screen updates

    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if pygame.mouse.get_pressed()[0]:
                try:

                    # User clicks the mouse. Get the position

                    pos = pygame.mouse.get_pos()

                    # Change the x/y screen coordinates to grid coordinates

                    column = pos[0] // (WIDTH_rect + MARGIN)
                    row = pos[1] // (HEIGHT_rect + MARGIN)

                    # Set that location to one

                    grid[row][column] = 1
                except:

                    pass
            if pygame.mouse.get_pressed()[2]:
                try:

                    # User clicks the mouse. Get the position

                    pos = pygame.mouse.get_pos()

                    # Change the x/y screen coordinates to grid coordinates

                    column = pos[0] // (WIDTH_rect + MARGIN)
                    row = pos[1] // (HEIGHT_rect + MARGIN)

                    # Set that location to one

                    grid[row][column] = 0
                except:
                    pass

        # Set the screen background

        screen.fill(BLACK)

        # Draw the grid

        for row in range(Wp):
            for column in range(Hp):
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN
                if grid[row][column] == 0:
                    color = WHITE
                pygame.draw.rect(screen, color,
                                 [(MARGIN + WIDTH_rect) * column + MARGIN,
                                  (MARGIN + HEIGHT_rect) * row + MARGIN,
                                  WIDTH_rect, HEIGHT_rect])

        # Limit to 60 frames per second

        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.

        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.

    pygame.quit()

    def update_text():
        x = open("text.txt")
        s = x.read().replace(",", '')
        x.close()

        x = open("text.txt", "w")
        x.write(s)
        x.close

        x = open("text.txt")
        st = x.read().replace("'", '')
        x.close()

        x = open("text.txt", "w")
        x.write(st)
        x.close

        x = open("text.txt")
        sts = x.read().replace("[", '')
        x.close()

        x = open("text.txt", "w")
        x.write(sts)
        x.close

        x = open("text.txt")
        stss = x.read().replace("]", "")
        x.close()

        x = open("text.txt", "w")
        x.write(stss)
        x.close

    with open('text.txt', 'a') as file:
        try:
            with open('text.txt', 'r') as reading:
                for a in reading:
                    if len(a) > 1:
                        with open('text.txt', 'w') as deleteing:
                            deleteing.write('')

            with open('text.txt', 'r+') as f:

                for i in grid:
                    for c in range(len(i)):
                        if i[c] == 0:
                            i[c] = '@'
                        else:
                            i[c] = '#'

                    if (len(i) + 1) % Wp:
                        f.write('\n')
                    f.write(str(i))

            update_text()

        except:
            with open('text.txt', 'r+') as f:

                for i in grid:
                    if (len(i) + 1) % Wp:
                        f.write('\n')
                    f.write(str(i))
            update_text()

    sys.exit()


def first_window():

    WIN = Tk()
    WIN.geometry('500x500')
    WIN.config(bg='black')
    Frame_bg = PhotoImage(file='Images\Frame 1.png')
    Label(WIN, image=Frame_bg).place(x=0, y=0)
    HEIGHT = StringVar()
    HEIGHT.set('250')
    WIDTH = StringVar()
    WIDTH.set('250')

    def clear_heignt(event):
        if HEIGHT.get() == '250':
            HEIGHT.set('')

    def clear_width(event):
        if WIDTH.get() == '250':
            WIDTH.set('')

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

    Warning = Label(WIN, font=('Arial', 15), bg='#48BEBF')
    Warning.place(x=145, y=365)

    def gen_windows():
        if int(HEIGHT.get()) < 100:
            Warning.config(text='Window height too small')
            Warning.place(x=145, y=365)
        elif int(WIDTH.get()) < 100:
            Warning.config(text='Window width too small')
            Warning.place(x=145, y=365)
        else:
            Warning.config(text='')
            WIN.withdraw()
            second_window(HEIGHT.get(), WIDTH.get())

    H = Entry(
        WIN,
        text=HEIGHT,
        font=('Arial', 25),
        width=4,
        bg='#42C9B5',
        fg='white',
        bd=0,
    )
    H.place(x=166, y=178)
    H.bind('<Button-1>', clear_heignt)
    H.bind('<Key>', check_height_val)

    W = Entry(
        WIN,
        text=WIDTH,
        font=('Arial', 25),
        width=4,
        bg='#44C5BB',
        fg='white',
        bd=0,
    )
    W.place(x=166, y=289)
    W.bind('<Button-1>', clear_width)
    W.bind('<Key>', check_width_val)

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
