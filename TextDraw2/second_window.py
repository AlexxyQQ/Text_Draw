import pygame
from tkinterPopup import popupmsg
import constants

def second_window():
    # Initialize Pygame
    pygame.init()

    # Changing variables
    Paint_Color = constants.GREEN
    Brush_Size = 1
    pointer = 1


    # Create the window
    screen = pygame.display.set_mode(constants.WINDOW_SIZE)

    # Create a 2D array to hold the state of each cell
    grid_state = [[0 for y in range(constants.GRID_SIZE)]
                for x in range(constants.GRID_SIZE)]

    # Draw the grid
    for x in range(constants.GRID_SIZE):
        for y in range(constants.GRID_SIZE):
            rect = pygame.Rect(x * constants.CELL_SIZE, y * constants.CELL_SIZE,
                            constants.CELL_SIZE, constants.CELL_SIZE)
            pygame.draw.rect(screen, constants.WHITE, rect)
            pygame.draw.rect(screen, constants.BLACK, rect, 1)

    #
    # Constant Items on screen which are not changing
    # Draw the reset button
    reset_rect = pygame.Rect(10, 900-80, 100, 50)
    pygame.draw.rect(screen, constants.RED, reset_rect)
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
    # Draw the Green button
    green_color_rect = pygame.Rect(360+60, 900-80, 50, 50)
    pygame.draw.rect(screen, constants.GREEN, green_color_rect)
    font = pygame.font.Font(None, 36)
    green_char = font.render("!", True, (255, 255, 255))
    green_char_rect = green_char.get_rect(center=green_color_rect.center)
    screen.blit(green_char, green_char_rect)
    # Draw the Red button
    red_color_rect = pygame.Rect(240, 900-80, 50, 50)
    pygame.draw.rect(screen, constants.RED, red_color_rect)
    font = pygame.font.Font(None, 36)
    red_char = font.render("@", True, (255, 255, 255))
    red_char_rect = red_char.get_rect(center=red_color_rect.center)
    screen.blit(red_char, red_char_rect)
    # Draw the Pink button
    pink_color_rect = pygame.Rect(240+60, 900-80, 50, 50)
    pygame.draw.rect(screen, constants.PINK, pink_color_rect)
    font = pygame.font.Font(None, 36)
    pink_char = font.render("#", True, (255, 255, 255))
    pink_char_rect = pink_char.get_rect(center=pink_color_rect.center)
    screen.blit(pink_char, pink_char_rect)
    # Draw the Yellow button
    yellow_color_rect = pygame.Rect(240+60+60, 900-80, 50, 50)
    pygame.draw.rect(screen, constants.YELLOW, yellow_color_rect)
    font = pygame.font.Font(None, 36)
    yellow_char = font.render("$", True, (255, 255, 255))
    yellow_char_rect = yellow_char.get_rect(center=yellow_color_rect.center)
    screen.blit(yellow_char, yellow_char_rect)


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
                # show a tkinter message box
                popupmsg("Length of characters?", "Export", grid_state)

        # Check if the reset button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and reset_rect.collidepoint(event.pos):
                # Reset the grid
                grid_state = [[0 for y in range(
                    constants.GRID_SIZE)] for x in range(constants.GRID_SIZE)]
                # Draw the grid
                for x in range(constants.GRID_SIZE):
                    for y in range(constants.GRID_SIZE):
                        rect = pygame.Rect(x * constants.CELL_SIZE, y *
                                        constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE)
                        pygame.draw.rect(screen, constants.WHITE, rect)
                        pygame.draw.rect(screen, constants.BLACK, rect, 1)
            # Check if the Red button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and red_color_rect.collidepoint(event.pos):
                Paint_Color = constants.RED
                pointer = 2
            # Check if the Pink button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and pink_color_rect.collidepoint(event.pos):
                Paint_Color = constants.PINK
                pointer = 3
            # Check if the Yellow button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and yellow_color_rect.collidepoint(event.pos):
                Paint_Color = constants.YELLOW
                pointer = 4
            # Check if the Green button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and green_color_rect.collidepoint(event.pos):
                Paint_Color = constants.GREEN
                pointer = 1

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
                cell_x, cell_y = x // constants.CELL_SIZE, y // constants.CELL_SIZE
                if 0 <= cell_x < constants.GRID_SIZE and 0 <= cell_y < constants.GRID_SIZE:
                    # Toggle the state of the clicked cell
                    for i in range(cell_x, min(cell_x + Brush_Size, constants.GRID_SIZE)):
                        for j in range(cell_y, min(cell_y + Brush_Size, constants.GRID_SIZE)):
                            grid_state[j][i] = pointer
                            # Update the color of the clicked cell and its 3 neighbors to the right, below, and below-right
                            rect = pygame.Rect(i * constants.CELL_SIZE, j *
                                            constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE)
                            pygame.draw.rect(
                                screen, Paint_Color, rect)
                            pygame.draw.rect(screen, constants.BLACK, rect, 1)
            elif pygame.mouse.get_pressed()[2]:
                # Check if a cell was clicked
                x, y = event.pos
                cell_x, cell_y = x // constants.CELL_SIZE, y // constants.CELL_SIZE
                if 0 <= cell_x < constants.GRID_SIZE and 0 <= cell_y < constants.GRID_SIZE:
                    # Toggle the state of the clicked cell
                    for i in range(cell_x, min(cell_x + Brush_Size, constants.GRID_SIZE)):
                        for j in range(cell_y, min(cell_y + Brush_Size, constants.GRID_SIZE)):
                            grid_state[j][i] = pointer
                            # Update the color of the clicked cell and its 3 neighbors to the right, below, and below-right
                            rect = pygame.Rect(i * constants.CELL_SIZE, j *
                                            constants.CELL_SIZE, constants.CELL_SIZE, constants.CELL_SIZE)
                            pygame.draw.rect(
                                screen, constants.WHITE, rect)
                            pygame.draw.rect(screen, constants.BLACK, rect, 1)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
