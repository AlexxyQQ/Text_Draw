import pygame

# Initialize Pygame
pygame.init()

# Set the size of the grid and the window
GRID_SIZE = 100
WINDOW_SIZE = (800, 800)

# Set the size of each cell in the grid
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

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

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
