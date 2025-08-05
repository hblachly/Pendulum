import math
'''
    Helper functions and constant variables not tied to any class 

    Colors: Constant 3 int tuples (int, int, int) representing the rgb value (RED, GREEN, BLUE)
'''

WHITE = (255, 255, 255)
BLACK = (0, 0 , 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Finds an angle from the x-axis to the line segment from the center_point to a point
# Parameters - point: (int x, int y), center_point: (int x, int y)
# Returns a float value representing the angle on the unit circle in degrees from -180 to 180
def get_angle(point, center_point):
    delta_x = point[0] - center_point[0]
    delta_y = point[1] - center_point[1]
    return math.degrees(math.atan2(delta_y, delta_x))

# Gets a point on a circle given its center, radius, and angle
# Parameters - center_point: (int x, int y), radius: int, angle: float
# Returns (int x, int y) pair representing a point on a circle at the angle given
def get_point_on_circle(center_point, radius, angle):
    x = center_point[0] + radius * math.cos(math.radians(angle)) # x value on unit circle scaled by length and offset by center_point[x]
    y = center_point[1] + radius * math.sin(math.radians(angle)) # y value on unit circle scaled by length and offset by center_point[y]
    return (round(x), round(y))

# Checks if a point is inside of a circle given the center and radius of the circle
# Parameters - point: (int x, int y), circle_center: (int x, int y): radius = float
# Returns a boolean value: True = inside circle - False = Outside Circle
def inside_circle(point, circle_center, radius):
    delta_x = point[0] - circle_center[0] # Difference in x values -> point[x] - circle_center[x]
    delta_y = point[1] - circle_center[1] # Difference in y values -> point[y] - circle_center[y]
    return radius >= math.sqrt(delta_x * delta_x + delta_y * delta_y) # Compare radius  against distance from center using distance formula