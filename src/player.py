import pygame.sprite
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN

from utils import randcolor

PLAYER_VELOCITY = 6


class Player(pygame.sprite.Sprite):
    COLOR = randcolor()

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0

    def handle_movement(self):
        keys = pygame.key.get_pressed()
        self.x_vel = 0
        self.y_vel = 0
        if keys[K_RIGHT]:
            self.move_right(PLAYER_VELOCITY)
        if keys[K_LEFT]:
            self.move_left(PLAYER_VELOCITY)
        if keys[K_UP]:
            self.move_up(PLAYER_VELOCITY)
        if keys[K_DOWN]:
            self.move_down(PLAYER_VELOCITY)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, velocity):
        self.x_vel = -velocity

    def move_right(self, velocity):
        self.x_vel = velocity

    def move_up(self, velocity):
        self.y_vel = -velocity

    def move_down(self, velocity):
        self.y_vel = velocity

    def loop(self):
        self.move(self.x_vel, self.y_vel)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)


class Enemy(pygame.sprite.Sprite):
    COLOR = randcolor()

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0

    def loop(self):
        self.COLOR = randcolor()

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
