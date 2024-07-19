import pygame as pg
import math
import random 

RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
pg.init()

pg.display.init()

screen = pg.display.set_mode((800, 800))
pg.display.set_caption("Cat aquarium")


class Sprite(pg.sprite.Sprite):
    def __init__(self, path: str, size: tuple[int | float, int | float], pos: tuple[int | float, int | float], *groups):
        super().__init__(*groups)
        self.image = pg.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.image = pg.transform.scale(self.image, size)

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Fish(Sprite):
    bounds = (0,800,0,800)
    def __init__(self, path: str,
                 size: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 speed: tuple[int | float, int | float],
                 *groups):
        super().__init__(path, size, pos, *groups)
        self.speed = speed

    def update(self, ):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.x == Fish.bounds[0] or self.rect.x == Fish.bounds[1] or self.rect.y == Fish.bounds[2] or self.rect.y == Fish.bounds[3]:
            self.speed[0] *= -1
            self.speed[1] *= -1
        
        # angle = math.atan(self.speed[0])
        # self.image = pg.transform.rotate(self.image, angle)


class Aquarium():
    def __init__(self, count, scren_width, screen_height):
        self.fishes = pg.sprite.Group()
        for i in range(count):
            size = random.randint(25,100)
            speed_x = random.randint(0,3)
            speed_y = random.randint(0,3)
            pos_y = random.randint(0,800)
            pos_x = random.choice([0,800])
            axolotl = Fish("Sprites/axolotl.png", (size*2, size), (pos_x, pos_y), [speed_x,speed_y])
            self.fishes.add(axolotl)
    def update(self, screen):
        self.fishes.update()
        self.fishes.draw(screen)



background = Sprite("Sprites/background.png", (800, 800), (0, 0))
aquarium = Aquarium(20,800,800)

running = True






while running:
    background.draw(screen)
    aquarium.update(screen)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    pg.display.update()
