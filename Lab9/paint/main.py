# Import the Pygame library
import pygame

# Define some colors as RGB tuples
white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Define the main function that will run the game
def main():

    # Initialize the Pygame library
    pygame.init()

    # Set the screen size to 640x480 pixels
    screen = pygame.display.set_mode((640, 480))

    # Create a clock to control the frame rate
    clock = pygame.time.Clock()

    # Initialize some variables for drawing
    radius = 15
    color = white
    last_pos = None

    # Start the main loop of the game
    while True:

        # Handle all events in the Pygame event queue
        for event in pygame.event.get():

            # If the user wants to quit, exit the program
            if event.type == pygame.QUIT:
                return

            # If the user presses the escape key, exit the program
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                # If the user presses the r, g, b, y, or space key, change the drawing color
                if event.key == pygame.K_q:
                    color = red
                elif event.key == pygame.K_w:
                    color = green
                elif event.key == pygame.K_e:
                    color = blue
                elif event.key == pygame.K_r:
                    color = yellow
                elif event.key == pygame.K_SPACE:
                    color = black

                # If the user presses the w or c key, draw a rectangle or circle at the mouse position
                elif event.key == pygame.K_t:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, color)
                elif event.key == pygame.K_y:
                    drawCircle(screen, pygame.mouse.get_pos(), color)
                elif event.key == pygame.K_u:
                    drawSquare(screen, pygame.mouse.get_pos(), 100, 100, color)
                elif event.key == pygame.K_i:
                    drawrighttriangle(screen, pygame.mouse.get_pos(), color)
                elif event.key == pygame.K_o:
                    draweqtriangle(screen, pygame.mouse.get_pos(), color)
                elif event.key == pygame.K_p:
                    drawrhombus(screen, pygame.mouse.get_pos(), color)

            # If the user clicks the left mouse button, start drawing a line
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()

            # If the user moves the mouse with the left button down, draw a line between the last position and the current position
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    drawLineBetween(screen, start_pos, end_pos, radius, color)
                    last_pos = end_pos

        # Update the screen
        pygame.display.flip()

        # Limit the frame rate to 60 frames per second
        clock.tick(60)

# Define a function that draws a line between two points with a given width and color
def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
        
# Define a function that draws a rectangle or circle at a given position      
def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3) 
def drawSquare(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def drawrighttriangle(screen, mouse_pos, color):
   x = mouse_pos[0]
   y = mouse_pos[1]
   pygame.draw.polygon(screen, color, ((x, y), (x, y + 100), (x + 100, y + 100)), 3)
def draweqtriangle(screen, mouse_pos, color):
   x = mouse_pos[0]
   y = mouse_pos[1]
   pygame.draw.polygon(screen, color, ((x, y), (x - 50, y + 100), (x + 50, y + 100)), 3)

def drawrhombus(screen, mouse_pos, color):
   x = mouse_pos[0]
   y = mouse_pos[1]
   pygame.draw.polygon(screen, color, ((x, y), (x - 50, y + 100), (x, y + 200), (x + 50, y + 100)), 3)

main()