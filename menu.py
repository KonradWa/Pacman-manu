import pygame as pg
from support import *
from text import *
import sys
import os

bg_color = (32, 40, 80)
border_color = (71, 89, 177)
black = pg.color.THECOLORS['white']


class Menu:
    def __init__(self, create_level, status="main"):
        # Function

        self.create_level = create_level
        # Game data
        self.current_menu = status
        # Display
        self.display_surface = pg.display.set_mode((screen_width, screen_height))
        px, py = self.display_surface.get_rect().center[0], self.display_surface.get_rect().center[1]-80
        print(px, py)
        self.menu_dict = {}
        # Sound
        # self.menu_sound = pg.mixer.Sound("assets/sound/menu.ogg")
        # Decorate
        # Menu type
        # Main
        self.main_menu = []
        text = Button("START THE GAME", black, bg_color, border_color, 220, 25, px, py, "play", 15, menu =True)
        self.main_menu.append(text)
        text1 = Button("CONTROL", black, bg_color, border_color, 220, 25, px, py + 30, "control", 15, menu =True)
        self.main_menu.append(text1)
        text2 = Button("CREDITS", black, bg_color, border_color, 220, 25, px, py + 60, "credits", 15, menu =True)
        self.main_menu.append(text2)
        text3 = Button("EXIT THE GAME", black, bg_color, border_color, 220, 25, px, py + 90, "exit", 15, menu =True)
        self.main_menu.append(text3)
        self.menu_dict["main"] = self.main_menu
        # Credits
        self.credits_menu = []
        text = Button("Pacman", black, bg_color, border_color, 250, 25, px, py, None, 15, menu =True)
        self.credits_menu.append(text)
        text = Button("By", black, bg_color, border_color, 250, 25, px, py + 30, None, 15, menu =True)
        self.credits_menu.append(text)
        text = Button("Magdalena", black, bg_color, border_color, 250, 25, px, py + 60, None, 15, menu =True)
        self.credits_menu.append(text)
        text = Button("Dębska", black, bg_color, border_color, 250, 25, px, py + 90, None, 15, menu =True)
        self.credits_menu.append(text)
        text = Button("RETURN", black, bg_color, border_color, 250, 25, px, py + 120, "return", 15, menu =True)
        self.credits_menu.append(text)
        self.menu_dict["credits"] = self.credits_menu
        # Control
        self.credits_menu = []
        text = Button("RIGHT ->", black, bg_color, border_color, 250, 25, px, py, None, 15, menu=True)
        self.credits_menu.append(text)
        text = Button("LEFT <-", black, bg_color, border_color, 250, 25, px, py + 30, None, 15, menu=True)
        self.credits_menu.append(text)
        text = Button("UP /\\", black, bg_color, border_color, 250, 25, px, py + 60, None, 15, menu=True)
        self.credits_menu.append(text)
        text = Button("DOWN \\/", black, bg_color, border_color, 250, 25, px, py + 90, None, 15, menu=True)
        self.credits_menu.append(text)
        text = Button("PAUSED/PLAY-SPACE", black, bg_color, border_color, 250, 25, px, py + 90, None, 15, menu=True)
        self.credits_menu.append(text)
        text = Button("RETURN", black, bg_color, border_color, 250, 25, px, py + 120, "return", 15, menu=True)
        self.credits_menu.append(text)
        self.menu_dict["control"] = self.credits_menu

    def collision(self):
        for button in self.menu_dict[self.current_menu]:
            if button.rect.collidepoint(pg.mouse.get_pos()):
                if button.status == "play":
                    self.create_level()
                    print("TEST")
                elif button.status == "menu":
                    self.current_menu = "main"
                elif button.status == "control":
                    self.current_menu = "control"
                elif button.status == "credits":
                    self.current_menu = "credits"
                elif button.status == "exit":
                    pg.quit()
                    sys.exit()
                elif button.status == "return":
                    self.current_menu = "main"

    def run(self):
        for button in self.menu_dict[self.current_menu]:
            button.draw(self.display_surface)
