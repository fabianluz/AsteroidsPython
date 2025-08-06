import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Call the parent class (CircleShape) constructor
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Draw the asteroid as a circle with a width of 2 pixels
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line at a constant speed
        self.position += self.velocity * dt