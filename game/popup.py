import pygame
import pygame.locals as const
from constants import path_inter, path_excla, path_bubble, start, bubble_pos


class Popup:
    """class displaying pop up"""
    def __init__(self, surface, hero, items):
        self.surface = surface
        self.hero = hero
        self.items = items
        # Loading images
        self.inter = pygame.image.load(path_inter).convert_alpha()
        self.excla = pygame.image.load(path_excla).convert_alpha()
        self.bubble = pygame.image.load(path_bubble).convert_alpha()
        # position images
        self.x = self.hero.position[0]
        self.y = self.hero.position[1]

    def renderPopUp(self, hero_position):
        """Display a little pop up image when you pick up an item"""
        self.x = hero_position[0]
        self.y = hero_position[1]
        if self.hero.position == start:
            self.surface.blit(self.inter, (self.x + 50, self.y))
        elif self.hero.position in self.items.list_pos:
            self.surface.blit(self.excla, (self.x + 50, self.y))
            self.items.list_pos.remove(self.hero.position)

    def render_message(self):
        """Display a instruction message"""
        if self.hero.position == start:
            self.surface.blit(self.bubble, bubble_pos)
