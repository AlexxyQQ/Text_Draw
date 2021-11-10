import pygame
import sys


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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    done = True

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

    # pygame.quit()
    Main_Functon()

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
                            i[c] = '  '
                        else:
                            i[c] = '@'

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

    # sys.exit()


pygame.init()
pygame.font.init()
# Create the screen

(WIDTH, HEIGHT) = (500, 500)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Title and Icon

pygame.display.set_caption("Text Draw")
Icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(Icon)

""" Images """
Background = pygame.image.load("Images/Frame 1.png")

Button_image = pygame.image.load('Images\Button Grn.png').convert_alpha()
Button_image_zoomed = pygame.transform.rotozoom(
    Button_image, 0, 1.05).convert_alpha()
Button_image_varied = Button_image


Height = pygame.image.load("Images\Height.png").convert_alpha()
Height_zoomed = pygame.transform.rotozoom(Height, 0, 1.05).convert_alpha()
Height_varied = Height

Width = pygame.image.load("Images\Width.png").convert_alpha()
Width_zoomed = pygame.transform.rotozoom(Width, 0, 1.05).convert_alpha()
Width_varied = Width


def Main_Functon():
    global Height_varied, Width_varied, Button_image_varied
    clock = pygame.time.Clock()
    FPS = 60
    running = True

    """a"""
    font = pygame.font.Font(None, 50)
    color_inactive = pygame.Color('Grey')
    color_active = pygame.Color('White')
    color_h = color_inactive
    color_w = color_inactive
    height_text_active = False
    width_text_active = False
    height_text = '250'
    width_text = "250"

    while running:
        clock.tick(FPS)
        WIN.blit(Background, (0, 0))

        """ Mouse Pos variable """
        pos = pygame.mouse.get_pos()

        """Image Transform Variables"""
        Height_rect = Height_varied.get_rect()
        Height_rect.topleft = (WIDTH/2 - Height_varied.get_width()/2,
                               (HEIGHT/2 - Height_varied.get_height()/2)-20)
        Width_rect = Width_varied.get_rect()
        Width_rect.topleft = (WIDTH/2 - Width_varied.get_width()/2,
                              (HEIGHT/2 - Width_varied.get_height()/2)+60)
        Button_image_rect = Button_image_varied.get_rect()
        Button_image_rect.topleft = (WIDTH/2 - Button_image_varied.get_width()/2,
                                     (HEIGHT/2 - Button_image_varied.get_height()/2)+200)
        """ Game event check """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if Height_rect.collidepoint(pos):
                Height_varied = Height_zoomed
            else:
                Height_varied = Height
            if Width_rect.collidepoint(pos):
                Width_varied = Width_zoomed
            else:
                Width_varied = Width
            if Button_image_rect.collidepoint(pos):
                Button_image_varied = Button_image_zoomed
            else:
                Button_image_varied = Button_image

            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if Button_image_rect.collidepoint(pos):
                    Button_image_varied = Button_image
                    second_window(int(height_text), int(width_text))

                if Height_rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    if height_text == '250':
                        height_text = ''

                    height_text_active = not height_text_active
                else:
                    height_text_active = False
                color_h = color_active if height_text_active else color_inactive

                if Width_rect.collidepoint(event.pos):
                    # Toggle the active variable.
                    if width_text == '250':
                        width_text = ''

                    width_text_active = not width_text_active
                else:
                    width_text_active = False
                color_w = color_active if width_text_active else color_inactive

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Button_image_varied = Button_image
                    second_window(int(height_text), int(width_text))

                if height_text_active:
                    if event.key == pygame.K_BACKSPACE:
                        height_text = height_text[:-1]
                    else:
                        height_text += event.unicode

                if width_text_active:
                    if event.key == pygame.K_BACKSPACE:
                        width_text = width_text[:-1]
                    else:
                        width_text += event.unicode

        WIN.blit(Height_varied, Height_rect)
        WIN.blit(Width_varied, Width_rect)
        WIN.blit(Button_image_varied, Button_image_rect)
        height_txt_surface = font.render(height_text, True, color_h)
        width_txt_surface = font.render(width_text, True, color_w)
        WIN.blit(height_txt_surface, (Height_rect.x+80, Height_rect.y+10))
        WIN.blit(width_txt_surface, (Width_rect.x+80, Width_rect.y+10))

        pygame.display.update()


if __name__ == "__main__":
    Main_Functon()
