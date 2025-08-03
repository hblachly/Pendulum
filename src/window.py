import pygame
'''
    Initializes a pygame window with given dimensions/title, handles events, and creates the main loop

    __init__ parameters:
        title = string
        width = int -> Default: 400
            -Note: Minimum > 0 -> Maximum <= Current Display Resolution width
        height = int -> Default: 300
            -Note: Minimum > 0 -> Maximum <= Current Display Resolution height
        color = (int, int, int) -> (RED, GREEN, BLUE)
            -Note: Minimum of 0: (0, 0, 0) -> Maximum of 255: (255, 255, 255)
        events = dictionary -> {key = pygame.EVENT : value = function}
            -Note: Exclude parentheses from functions or use lambda function 
                -Ex: {pygame.QUIT, quit} or {pygame.QUIT, lambda: function(parameter)}

    Member vars:
        WHITE = constant int tuple (RED,GREEN,BLUE) -> represents the color white
        screen = pygame display screen
        running = boolean -> True = running / False = exiting
        width = Window screen width
        height = Window screen height
        color = Background color Default: WHITE or (255,255,255)
        events = Links pygame events to functions
        draw_functions = list to append lambda functions that draw to screen each loop
            -Ex: screen.append(lambda: draw(screen))

'''
class Window:
    WHITE = (255, 255, 255)

    # initialize pygame, sets up the screen, and defines member variables
    def __init__(self, title = "Window", width = 400, height = 300, color = WHITE, events = {}):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.width = width
        self.height = height
        self.color = color
        self.events = events
        self.draw_functions = []

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
                self.events[event.type]() # Runs functions paired with the pygame event type

    # Handles drawing to screen for each loop by filing the background, calling draw functions, and updating the display window
    def draw(self):
        self.screen.fill(self.color)
        for function in self.draw_functions:
            function()
        pygame.display.update()

    # Creates main loop, handle user input events, update screen, and quit after running = False
    def main_loop(self):
        while(self.running):
            self.handle_events()
            self.draw()

        pygame.quit()