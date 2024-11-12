import random
import math
import pygame
from circleshape import CircleShape

import pygame
import random
import math
from circleshape import CircleShape

import pygame
import random
import math
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call the superclass initializer
        angle_degrees = random.uniform(0, 360)
        angle_radians = math.radians(angle_degrees)
        speed = random.uniform(40, 100)
        self.velocity = pygame.Vector2(math.cos(angle_radians) * speed, math.sin(angle_radians) * speed)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        