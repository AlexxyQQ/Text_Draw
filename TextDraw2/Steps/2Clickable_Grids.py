import pygame

# Initialize Pygame
pygame.init()

# Set the size of the grid and the window
GRID_SIZE = 10
WINDOW_SIZE = (800, 800)

# Set the size of each cell in the grid
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE

# Set the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Create a 2D array to hold the state of each cell
grid_state = [[False for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

# Draw the grid
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                grid_state[cell_x][cell_y] = not grid_state[cell_x][cell_y]
                # Update the color of the clicked cell
                color = GREEN
                rect = pygame.Rect(cell_x * CELL_SIZE,
                                   cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
        elif pygame.mouse.get_pressed()[2]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                grid_state[cell_x][cell_y] = not grid_state[cell_x][cell_y]
                # Update the color of the clicked cell
                color = WHITE
                rect = pygame.Rect(cell_x * CELL_SIZE,
                                   cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
