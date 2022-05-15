# Import pygame library for display configuration
# Import os for system retrieves

import pygame
import os

# Setting display up
# First display will called screen
# This first screen will have 640X480 pixels, 0 flaging
screen = pygame.display.set_mode((640, 480), 0)

# Creating first object
x = 10
y = 10
velocity = 1

velocity_x = velocity
velocity_y = velocity


# Function to return color object
def get_color(color_name):
    if color_name == "yellow":
        return (255, 255, 0)
    if color_name == "black":
        return (0, 0, 0)
    if color_name == "white":
        return (255, 255, 255)


# keep the display open:
while True:
    #removing traces
    screen.fill(get_color("black"))

    # Movement rules

    x = x + velocity_x * 0.2
    y = y + velocity_y * 0.1

    if x > 640:
        velocity_x = -velocity
    if x < 0:
        velocity_x = velocity

    if y > 480:
        velocity_y = -velocity
    if y < 0:
        velocity_y = velocity


    # Moving objects
    pacman = pygame.draw.circle(surface=screen, color=get_color("yellow"), center=(x, y), radius=10, width=3)
    pygame.display.update()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
