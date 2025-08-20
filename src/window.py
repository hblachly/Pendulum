import pygame
from utilities import WHITE
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
        fps = int -> Default: 60
            -Note: Min = 0 = no fps cap

    Member vars:
        screen = pygame display screen
        width = Window screen width
        height = Window screen height
        color = Background color Default: WHITE or (255,255,255)
        events = Links pygame events to functions
        update_functions = list to append functions that are called each loop
            -Ex: window.update_functions.append(pendulum.update)
        fps = Number of times the main loop should run per second at most

        Private Variables:
        _running = boolean -> True = running / False = exiting
        _clock = pygame Clock allows for more precise number of executions of the main loop per second
            -Note: Limits execution of main loop to number of frames per second or fps

'''
class Window:

    # initialize pygame, sets up the screen, and defines member variables
    def __init__(self, title = "Window", width = 400, height = 300, color = WHITE, events = {}, fps = 60):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height
        self.color = color
        self.events = events
        self.update_functions = []
        self.fps = fps

        # Private variables
        self._running = True
        self._clock = pygame.time.Clock()
    
    # Creates main loop, handle user input events, update screen, and quit after running = False
    def main_loop(self):
        while(self._running):
            self._clock.tick(self.fps) # Number of loops executed per second = fps
            self._handle_events()
            self._update()

        pygame.quit()

    # Add a function to update_functions
    def add_update_function(self, function):
        if callable(function):
            self.update_functions.append(function)

    # Map a pygame event to a function by adding a {key = pygame_events : value = function} pair to events
    def add_event(self, pygame_event, function):
        if callable(function):
            self.events[pygame_event] = function

    # Private Functions

    def _quit(self):
        print("Exiting Window")
        self._running = False

    # Handle pygame events for user input
    # Adds default quit function in events if pygame.QUIT is not found in events
    # When a pygame event is found as a key -> Runs function found as the value at that key
    def _handle_events(self):
        if pygame.QUIT not in self.events:
            print("Adding quit Key : Value to dictionary")
            self.events[pygame.QUIT] = self._quit

        for event in pygame.event.get():
            if event.type in self.events:
                self.events[event.type]() # Runs functions paired with the pygame event type

    # Handles updates by filling the background, calling functions, and updating the display window for each loop
    def _update(self):
        self.screen.fill(self.color)
        for function in self.update_functions:
            function()
        pygame.display.update()