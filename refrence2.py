import pygame

H = 700
W = 700
P = 50

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
for row in range(Hp):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(Wp):
        grid[row].append(0)  # Append a cell

# Initialize pygame
pygame.init()

# Set the HEIGHT_rect and WIDTH_rect of the screen
WINDOW_SIZE = [H, W]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

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
                print("Click ", pos, "Grid coordinates: ", row, column)
            except:
                pass

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid
    for row in range(Hp):
        for column in range(Wp):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
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