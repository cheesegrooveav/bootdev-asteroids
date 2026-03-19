import pygame
import player
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    field = AsteroidField()
    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1 == 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        player1.shot_cooldown -= dt
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
