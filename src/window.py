import pygame
'''
    Initializes a pygame window with given dimensions/title, handles events, and creates the main loop

    __init__ paramseter:
        title = string - Title of the screen default: "Window"
        width = int: width of screen default: 400
        height = int: height of screen default: 300
        color = int tuple (RED, GREEN, BLUE) - Background Color default: WHITE or (255,255,255)

    Extra member vars:
        WHITE = constant int tuple (RED,GREEN,BLUE) for white
        screen = pygame display screen
        running = boolean - True = running / False = exiting
'''
class Window:
    WHITE = (255, 255, 255)

    #initialize pygame window,screen, and member variables
    def __init__(self, title = "Window", width = 400, height = 300, color = WHITE):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.color = color
        self.running = True

    #Handle pygame events for user input
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    #Creates main loop, handle user input events, update screen, and quit after running = False
    def main_loop(self):
        while(self.running):
            self.handle_events()
            self.screen.fill(self.color)
            pygame.display.flip()

        pygame.quit()