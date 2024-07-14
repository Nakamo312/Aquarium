import pygame as pg
import math

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
    def __init__(self, path: str,
                 size: tuple[int | float, int | float],
                 pos: tuple[int | float, int | float],
                 speed: tuple[int | float, int | float],
                 *groups):
        super().__init__(path, size, pos, *groups)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        # angle = math.atan(self.speed[0])
        # self.image = pg.transform.rotate(self.image, angle)

background = Sprite("Sprites/background.png", (800, 800), (0, 0))
axolotl = Fish("Sprites/axolotl.png", (200, 100), (100, 200), (1,1))
running = True

while running:
    background.draw(screen)
    axolotl.update()
    axolotl.draw(screen)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

    pg.display.update()
