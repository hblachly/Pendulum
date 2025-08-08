import pygame
import utilities
import math

'''
    Allows a Pendulum to be drawn on a Window screen and simulates it's physics at different angles

    __init__  parameters:
        origin: (int, int)
        length: int
        radius: int
        angle: float

    Member Variables:
        origin: Anchor point at which to draw the pendulum
        length: length of pendulum from origin point
        radius: Circle radius of mass drawn to end of pendulum
        angle: The current angle of the pendulum in degrees
            -Note: angle is reverse of unit circle due to y-axis being in reverse for screen coordinates
            -Ex: 90 degrees on unit circle where y=1 means the pendulum should be above the origin but instead it is below the origin
        mass_center: The point representing the center of the circle at end of the pendulum
        holding: Whether the mouse is held down on the circle at the end of the pendulum
        time: the amount of time passed while not holding in increments of 1/fps of a second
        amplitude: Angle displacement or change from the equilibrium angle of 90 degrees
            -Note: negative to the right and positive to the left
'''

class Pendulum:
    
    # Initialize class and define member variables
    def __init__(self, origin = (10, 4), length = 15, radius = 10, angle = 90):
        self.origin = origin
        self.length = length
        self.radius = radius
        self.angle = angle
        self.mass_center = (self.origin[0], self.origin[1] + length)
        self.holding = False
        self.time = 0.0
        self.amplitude = 0.0

    # Setter function for holding if inside circle
    def set_holding(self, holding):
        self.holding = holding
        mouse_position = pygame.mouse.get_pos()
        if not utilities.inside_circle(mouse_position, self.mass_center, self.radius):
            self.holding = False

    # Draw Pendulum to Window screen
    def draw(self, screen):
        pygame.draw.line(screen, utilities.BLACK, self.origin, self.mass_center) # Attachment to mass
        pygame.draw.circle(screen, utilities.RED, self.origin, 4) # Anchor point
        pygame.draw.circle(screen, utilities.BLACK, self.mass_center, self.radius) # Mass circle outline
        pygame.draw.circle(screen, utilities.WHITE, self.mass_center, self.radius - 2) # Mass circle Fill

    # Updates the amplitude and time while holding and then updates the angle when dropped using the small angle approximation formula
    def angle_time_approximation(self):
        if self.holding:
            self.amplitude = self.angle - 90
            if self.amplitude < -180: # Keeps the amplitude ranging from -180 to 180
                self.amplitude += 360
            self.time = 0.0

        else:
            meter_length = self.length / 100
            angular_frequency = math.sqrt(utilities.GRAVITY / meter_length)
            self.angle = 90 + self.amplitude * math.cos(angular_frequency * self.time) # Equilibrium angle of 90 degrees + small angle approximation formula
            self.time += 1 / 60

    # Update the pendulum's state / member variables
    def update(self):
        if self.holding:
            mouse_position = pygame.mouse.get_pos()
            self.angle = utilities.get_angle(mouse_position, self.origin)

        self.angle_time_approximation()
        self.mass_center = utilities.get_point_on_circle(self.origin, self.length, self.angle)