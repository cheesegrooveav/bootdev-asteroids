from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, PLAYER_SHOOT_SPEED, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.rotation = 0


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)