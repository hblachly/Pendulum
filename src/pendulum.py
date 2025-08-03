import pygame
import math
from window import Window

'''
    Allows a Pendulum to be drawn on a Window screen and simulates it's physics at different angles

    __init__  parameters:
        origin: (int, int)
        length: int
        radius: int
        angle: double

    Member Variables:
        origin: Anchor point at which to draw the pendulum
        length: length of pendulum from origin point
        radius: Circle radius of mass drawn to end of pendulum
        angle: The current angle of the pendulum in degrees
            -Note: angle is reverse of unit circle due to y-axis being in reverse for screen coordinates
            -Ex: 90 degrees on unit circle where y=1 means the pendulum should be above the origin but instead it is below the origin
        mass_center: The point representing the center of the circle at end of the pendulum
        holding: Whether the mouse is held down on the circle at the end of the pendulum
'''

# Takes the difference between two points and finds the angle based on the change
def get_new_angle(new_point, old_point):
    return math.degrees(math.atan2(new_point[1] - old_point[1], new_point[0] - old_point[0]))

# Gets the center of a circle at a distance = length from the point = orign at the angle along a unit circle
def get_circle_center(origin, length, angle):
    x = origin[0] + length * math.cos(math.radians(angle))
    y = origin[1] + length * math.sin(math.radians(angle))
    return (math.floor(x), math.floor(y))

class Pendulum:
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Initialize class and define member variables
    def __init__(self, origin = (10, 4), length = 15, radius = 10, angle = 90):
        self.origin = origin
        self.length = length
        self.radius = radius
        self.angle = angle
        self.mass_center = (self.origin[0], self.origin[1] + length)
        self.holding = False

    # Setter function for holding
    def set_holding(self, holding):
        self.holding = holding
        print ("Holding = ", holding)

    # Draw Pendulum to Window screen
    def draw(self, screen):
        pygame.draw.line(screen, self.BLACK, self.origin, self.mass_center) # Attachment to mass
        pygame.draw.circle(screen, self.RED, self.origin, 4) # Anchor point
        pygame.draw.circle(screen, self.BLACK, self.mass_center, self.radius) # Mass circle outline
        pygame.draw.circle(screen, self.WHITE, self.mass_center, self.radius - 2) # Mass circle Fill

    # Update the pendulum's state / member variables
    def update(self):
        if self.holding:
            mouse_position = pygame.mouse.get_pos()
            self.angle = get_new_angle(mouse_position, self.origin)
            print(self.angle)
        self.mass_center = get_circle_center(self.origin, self.length, self.angle)

pendulum = Pendulum(origin=(600, 250), length = 200, radius=25)
window = Window("Pendulum", width = 1200, height = 800)
window.draw_functions.append(lambda: pendulum.draw(window.screen))
window.draw_functions.append(pendulum.update)
window.events[pygame.MOUSEBUTTONDOWN] = lambda: pendulum.set_holding(True)
window.events[pygame.MOUSEBUTTONUP] = lambda: pendulum.set_holding(False)
window.main_loop()