import pygame 

from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,255))

    pygame.init()
if __name__ == "__main__":
    main()
