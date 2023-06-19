import pygame as pg
from support import *
from level import Level
from menu import Menu
import sys

class Game:
    def __init__(self):
        self.level = None
        self.menu = Menu(self.create_level)
        self.status = 'menu'

    def create_menu(self):
        self.menu = Menu( self.create_level)
        self.level.start_sound.stop()
        self.level.pacman_win_sound.stop()
        self.status = 'menu'

    def create_level(self):
        self.level = Level(self.create_menu)
        self.status = 'level'

    def run(self):
        if self.status == "menu":
            self.menu.run()
        elif self.status == "level":
            self.level.run()

pg.init()
screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
game = Game()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and game.status == "menu":
            game.menu.collision()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                game.create_menu()

    screen.fill((41, 49, 65))
    game.run()

    pg.display.update()
    clock.tick(150)
