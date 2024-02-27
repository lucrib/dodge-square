import pygame
from pygame.locals import (
    KEYDOWN,
    QUIT,
    K_ESCAPE,
)

from player import Player, Enemy

RED_COLOR = (255, 0, 0)

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60
PLAYER_SIZE = 30
pygame.init()

# Set up the drawing window
window = pygame.display.set_mode(SCREEN_SIZE)


def draw(surface, player, enemy):
    surface.fill((0, 0, 0))
    player.draw()
    enemy.draw()
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    player = Player(0, 0, PLAYER_SIZE, PLAYER_SIZE, window)
    enemy = Enemy(
        window.get_rect().centerx,
        window.get_rect().centery,
        PLAYER_SIZE,
        PLAYER_SIZE,
        window,
    )
    # Run until the user asks to quit
    running = True
    while running:
        clock.tick(FPS)
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        player.loop()
        enemy.loop()
        player.handle_movement()
        draw(window, player, enemy)

    # Done! Time to quit.
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
