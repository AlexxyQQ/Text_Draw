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

    pygame.display.set_caption('Text Draw')
    icon = pygame.image.load('Images/icon.png')
    pygame.display.set_icon(icon)

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

