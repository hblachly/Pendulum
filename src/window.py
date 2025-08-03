import pygame
'''
    Initializes a pygame window with given dimensions/title, handles events, and creates the main loop

    __init__ paramseter:
        title = string - Title of the screen default: "Window"
        width = int: width of screen default: 400
        height = int: height of screen default: 300
        color = int tuple (RED, GREEN, BLUE) - Background Color default: WHITE or (255,255,255)
        events = dictionary{pygame.EVENT : function} -> Links pygame events to functions
            (Note: give function name without parentheses - Ex: {pygame.QUIT : quit} instead of {pygame.Quit : quit()})

    Extra member vars:
        WHITE = constant int tuple (RED,GREEN,BLUE) for white
        screen = pygame display screen
        running = boolean - True = running / False = exiting
'''
class Window:
    WHITE = (255, 255, 255)

    # initialize pygame window,screen, and member variables
    def __init__(self, title = "Window", width = 400, height = 300, color = WHITE, events = {}):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.width = width
        self.height = height
        self.color = color
        self.events = events

    def quit(self):
        print("Exiting Window")
        self.running = False

    # Handle pygame events for user input
    # Adds default quit function in events if pygame.QUIT is not found in events
    # When a pygame event is found as a key -> Runs function found as the value at that key
    def handle_events(self):
        if pygame.QUIT not in self.events:
            print("Adding quit Key : Value to dictionary")
            self.events[pygame.QUIT] = self.quit

        for event in pygame.event.get():
            if event.type in self.events:
                self.events[event.type]() 

    # Creates main loop, handle user input events, update screen, and quit after running = False
    def main_loop(self):
        while(self.running):
            self.handle_events()
            self.screen.fill(self.color)
            pygame.display.flip()

        pygame.quit()

def mouse_down():
    print("Mouse Down")

def mouse_up():
    print("Mouse Up")

window_a = Window("Test Window A", events={pygame.MOUSEBUTTONDOWN : mouse_down, pygame.MOUSEBUTTONUP : mouse_up})
window_a.main_loop()