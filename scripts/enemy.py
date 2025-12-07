import pygame as pgm
import random as rd


class SmallEnemy(pgm.sprite.Sprite):
    def __init__(self, bg_size):
        super().__init__()

        self.image = pgm.image.load("images/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-5 * self.height, 0)

    def reset(self):
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-5 * self.height, 0)

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()


class MidEnemy(SmallEnemy):
    def __init__(self, bg_size):
        super().__init__(bg_size)

        self.image = pgm.image.load("images/enemy2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 1
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-10 * self.height, -self.height)

    def reset(self):
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-10 * self.height, -self.height)


class BigEnemy(SmallEnemy):
    def __init__(self, bg_size):
        super().__init__(bg_size)

        self.image1 = pgm.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pgm.image.load("images/enemy3_n2.png").convert_alpha()
        self.rect = self.image1.get_rect()
        self.speed = 1
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-15 * self.height, -5 * self.height)

    def reset(self):
        self.rect.left, self.rect.top = rd.randint(0, self.width - self.rect.width), rd.randint(-15 * self.height, -5 * self.height)
