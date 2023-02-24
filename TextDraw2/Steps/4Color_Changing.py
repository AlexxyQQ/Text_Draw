import pygame

# Initialize Pygame
pygame.init()

# Set the size of the grid and the window
GRID_SIZE = 50
WINDOW_SIZE = (800, 900)

# Set the size of each cell in the grid
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE

# Set the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PINK = (243, 100, 148)
YELLOW = (255, 200, 0)
Paint_Color = GREEN


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

# Draw the reset button
reset_rect = pygame.Rect(10, 900-80, 100, 50)
pygame.draw.rect(screen, RED, reset_rect)
font = pygame.font.Font(None, 36)
text = font.render("Reset", True, (255, 255, 255))
text_rect = text.get_rect(center=reset_rect.center)
screen.blit(text, text_rect)

# Draw the Color text
color_text_rect = pygame.Rect(10+100+20, 900-70, 100, 50)
pygame.draw.rect(screen, (0, 0, 0), color_text_rect)
font = pygame.font.Font(None, 36)
color_text = font.render("Colors : ", True, (255, 255, 255))
screen.blit(color_text, color_text_rect)


# Draw the Red button
red_color_rect = pygame.Rect(240, 900-80, 50, 50)
pygame.draw.rect(screen, RED, red_color_rect)
font = pygame.font.Font(None, 36)
red_char = font.render("R", True, (255, 255, 255))
red_char_rect = red_char.get_rect(center=red_color_rect.center)
screen.blit(red_char, red_char_rect)


# Draw the Pink button
pink_color_rect = pygame.Rect(240+60, 900-80, 50, 50)
pygame.draw.rect(screen, PINK, pink_color_rect)
font = pygame.font.Font(None, 36)
pink_char = font.render("P", True, (255, 255, 255))
pink_char_rect = pink_char.get_rect(center=pink_color_rect.center)
screen.blit(pink_char, pink_char_rect)


# Draw the Yellow button
yellow_color_rect = pygame.Rect(240+60+60, 900-80, 50, 50)
pygame.draw.rect(screen, YELLOW, yellow_color_rect)
font = pygame.font.Font(None, 36)
yellow_char = font.render("Y", True, (255, 255, 255))
yellow_char_rect = yellow_char.get_rect(center=yellow_color_rect.center)
screen.blit(yellow_char, yellow_char_rect)

# Draw the Green button
green_color_rect = pygame.Rect(360+60, 900-80, 50, 50)
pygame.draw.rect(screen, GREEN, green_color_rect)
font = pygame.font.Font(None, 36)
green_char = font.render("G", True, (255, 255, 255))
green_char_rect = green_char.get_rect(center=green_color_rect.center)
screen.blit(green_char, green_char_rect)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
         # Check if the reset button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and reset_rect.collidepoint(event.pos):
            # Reset the grid
            grid_state = [[False for y in range(
                GRID_SIZE)] for x in range(GRID_SIZE)]
            # Draw the grid
            for x in range(GRID_SIZE):
                for y in range(GRID_SIZE):
                    rect = pygame.Rect(x * CELL_SIZE, y *
                                       CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, WHITE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 1)
        # Check if the Red button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and red_color_rect.collidepoint(event.pos):
            Paint_Color = RED
        # Check if the Pink button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and pink_color_rect.collidepoint(event.pos):
            Paint_Color = PINK
        # Check if the Yellow button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and yellow_color_rect.collidepoint(event.pos):
            Paint_Color = YELLOW
        elif event.type == pygame.MOUSEBUTTONDOWN and green_color_rect.collidepoint(event.pos):
            Paint_Color = GREEN

        
        elif pygame.mouse.get_pressed()[0]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                grid_state[cell_x][cell_y] = not grid_state[cell_x][cell_y]
                # Update the color of the clicked cell
                rect = pygame.Rect(cell_x * CELL_SIZE,
                                   cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, Paint_Color, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)
        elif pygame.mouse.get_pressed()[2]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                grid_state[cell_x][cell_y] = not grid_state[cell_x][cell_y]
                # Update the color of the clicked cell
                rect = pygame.Rect(cell_x * CELL_SIZE,
                                   cell_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
