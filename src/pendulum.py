import pygame
from window import Window

'''
    Allows a Pendulum to be drawn on a Window screen and simulates it's physics at different angles

    __init__  parameters:
        origin: (int, int)
        length: int
        radius: int

    Member Variables:
        origin: point at which to draw the pendulum
        length: length of pendulum from origin point
        radius: Circle radius drawn to end of pendulum
'''

class Pendulum:
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Initialize class and define member variables
    def __init__(self, origin = (10, 4), length = 15, radius = 10):
        self.origin = origin
        self.length = length
        self.radius = radius

    # Draw Pendulum to Window screen
    def draw(self, screen):
        end_point = (self.origin[0], self.origin[1] + self.length)
        pygame.draw.line(screen, self.BLACK, self.origin, end_point)
        pygame.draw.circle(screen, self.RED, self.origin, 4)
        pygame.draw.circle(screen, self.BLACK, end_point, self.radius)
        pygame.draw.circle(screen, self.WHITE, end_point, self.radius - 2)

    def update(self):
        # Update the pendulum's state / member variables
        pass

pendulum = Pendulum(origin=(200, 4), length = 200, radius=25)
window = Window("Pendulum")
window.draw_functions.append(lambda: pendulum.draw(window.screen))
window.main_loop()