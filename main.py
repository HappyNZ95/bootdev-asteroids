import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /  2)
    asteroidfield = AsteroidField()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit()

        screen.fill("black")

        updatable.update(dt)
        for member in drawable:
            member.draw(screen)

        pygame.display.flip()
        clock.tick(60)

        dt = clock.tick(60) / 1000
        player.update(dt)

    pygame.quit()


if __name__ == "__main__":
    main()
