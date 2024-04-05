# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:52:52 2024

@author: iamrs
"""

import time
import turtle

class Satellite:
    def __init__(self, name):
        self.name = name
        self.position = (0, 0)  # Initial position in space
        self.screen = turtle.Screen()
        self.screen.title("Satellite Movement")
        self.pen = turtle.Turtle()
        self.pen.speed(1)
        self.pen.penup()

    def move_to_mars(self):
        print(f"Sending satellite {self.name} to Mars...")
        self.pen.goto(self.position)
        self.pen.pendown()
        self.pen.write(f"Sending satellite {self.name} to Mars...", align="center")
        time.sleep(1)  # Simulating travel time
        self.position = (100, 100)  # New position near Mars
        self.pen.goto(self.position)
        self.pen.write(f"Satellite {self.name} has reached Mars!", align="center")

# Create a satellite object
mars_satellite = Satellite("MarsSatellite1")

# Send the satellite to Mars
mars_satellite.move_to_mars()

# Print the final position of the satellite
print(f"{mars_satellite.name} position after reaching Mars: {mars_satellite.position}")

# Keep the window open
mars_satellite.screen.mainloop()
