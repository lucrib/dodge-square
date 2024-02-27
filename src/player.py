import pygame
from pygame import K_RIGHT, K_LEFT, K_UP, K_DOWN, Surface, Rect
from pygame.sprite import Sprite

from utils import randcolor

PLAYER_VELOCITY = 6


class Player(Sprite):
    COLOR = randcolor()

    def __init__(self, x, y, width, height, window):
        super().__init__()
        self.rect = Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.window: Surface = window

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
        if self.rect.left < self.window.get_rect().left:
            self.rect.left = self.window.get_rect().left

    def move_right(self, velocity: int):
        self.x_vel = velocity
        if self.rect.right > self.window.get_rect().right:
            self.rect.right = self.window.get_rect().right

    def move_up(self, velocity):
        self.y_vel = -velocity
        if self.rect.top < self.window.get_rect().top:
            self.rect.top = self.window.get_rect().top

    def move_down(self, velocity):
        self.y_vel = velocity
        if self.rect.bottom > self.window.get_rect().bottom:
            self.rect.bottom = self.window.get_rect().bottom

    def loop(self):
        self.move(self.x_vel, self.y_vel)

    def draw(self):
        pygame.draw.rect(self.window, self.COLOR, self.rect)


class Enemy(pygame.sprite.Sprite):
    COLOR = randcolor()

    def __init__(self, x, y, width, height, window):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.window = window

    def loop(self):
        self.COLOR = randcolor()

    def draw(self):
        pygame.draw.rect(self.window, self.COLOR, self.rect)
