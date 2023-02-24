import matplotlib.pyplot as plt
import pygame

# Initialize Pygame
pygame.init()

# Set the size of the grid and the window
GRID_SIZE = 10
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
Brush_Size = 1


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

#
# Constant Items on screen which are not changing
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

# Draw the Pen Size
# Draw increament
pen_size_increament_rect = pygame.Rect(600, 900-80, 50, 50)
pygame.draw.rect(screen, (0, 0, 0), pen_size_increament_rect)
font = pygame.font.Font(None, 36)
pen_size_increament_char = font.render("+", True, (255, 255, 255))
pen_size_increament_char_rect = pen_size_increament_char.get_rect(
    center=pen_size_increament_rect.center)
screen.blit(pen_size_increament_char, pen_size_increament_char_rect)
# Draw decreament
pen_size_decreament_rect = pygame.Rect(600+60+60, 900-80, 50, 50)
pygame.draw.rect(screen, (0, 0, 0), pen_size_decreament_rect)
font = pygame.font.Font(None, 36)
pen_size_decreament_char = font.render("-", True, (255, 255, 255))
pen_size_decreament_char_rect = pen_size_decreament_char.get_rect(
    center=pen_size_decreament_rect.center)
screen.blit(pen_size_decreament_char, pen_size_decreament_char_rect)


# Run the game loop
running = True
while running:
    #
    # Changing items on screen
    # Update the brush size
    pen_size_value_rect = pygame.Rect(600+60, 900-80, 50, 50)
    pygame.draw.rect(screen, (0, 0, 0), pen_size_value_rect)
    font = pygame.font.Font(None, 36)
    pen_size_value_char = font.render(str(Brush_Size), True, (255, 255, 255))
    pen_size_value_char_rect = pen_size_value_char.get_rect(
        center=pen_size_value_rect.center)
    screen.blit(pen_size_value_char, pen_size_value_char_rect)
    #
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
        # Check if the Green button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and green_color_rect.collidepoint(event.pos):
            Paint_Color = GREEN

        # Check if the Pen Size Increament button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and pen_size_increament_rect.collidepoint(event.pos):
            if Brush_Size < 10:
                Brush_Size += 1
        # Check if the Pen Size Decreament button was clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and pen_size_decreament_rect.collidepoint(event.pos):
            if Brush_Size > 1:
                Brush_Size -= 1

        elif pygame.mouse.get_pressed()[0]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                for i in range(cell_x, min(cell_x + Brush_Size, GRID_SIZE)):
                    for j in range(cell_y, min(cell_y + Brush_Size, GRID_SIZE)):
                        grid_state[i][j] = True
                        # Update the color of the clicked cell and its 3 neighbors to the right, below, and below-right
                        rect = pygame.Rect(i * CELL_SIZE, j *
                                           CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            screen, Paint_Color, rect)
                        pygame.draw.rect(screen, BLACK, rect, 1)
        elif pygame.mouse.get_pressed()[2]:
            # Check if a cell was clicked
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if 0 <= cell_x < GRID_SIZE and 0 <= cell_y < GRID_SIZE:
                # Toggle the state of the clicked cell
                for i in range(cell_x, min(cell_x + Brush_Size, GRID_SIZE)):
                    for j in range(cell_y, min(cell_y + Brush_Size, GRID_SIZE)):
                        grid_state[i][j] = False

                        # Update the color of the clicked cell and its 3 neighbors to the right, below, and below-right
                        rect = pygame.Rect(i * CELL_SIZE, j *
                                           CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(
                            screen, WHITE, rect)
                        pygame.draw.rect(screen, BLACK, rect, 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
def create_text():
    with open ('text.txt', 'w') as f:
        for i in grid_state:
            for j in i:
                if j:
                    f.write(' ')
                else:
                    f.write('0')
            f.write('\n')

create_text()