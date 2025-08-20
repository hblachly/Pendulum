import pygame
from window import Window
from pendulum import Pendulum

def main():
    window = Window("Pendulum", 1200, 800, fps= 60) # Initialize new window with dimensions 1200x800
    pendulum = Pendulum(origin=(600, 250), length = 200, radius=25) # Initialize pendulum at x = 600 y = 250
    window.add_update_function(lambda: pendulum.draw(window.screen)) # Appends lambda function for drawing the pendulum to the screen
    window.add_update_function(lambda: pendulum.update(2)) # Appends pendulum function to updates variables using type 1 or 2 update function
    window.add_event(pygame.MOUSEBUTTONDOWN, lambda: pendulum.set_holding(True)) # Sets holding to True on mouse up event by adding to events
    window.add_event(pygame.MOUSEBUTTONUP, lambda: pendulum.set_holding(False)) # Sets holding to False on mouse up event by adding to events
    window.main_loop()

main()