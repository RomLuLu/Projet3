import pygame
import pygame.locals as const
from constants import *
import random


class Item:
    def __init__(self, screen, level, hero):
        self.screen = screen
        self.level = level
        self.hero = hero
        # Loading images.
        self.needle = pygame.image.load(path_needle).convert_alpha()
        self.ether = pygame.image.load(path_ether).convert_alpha()
        self.syringe = pygame.image.load(path_syringe).convert_alpha()
        self.tube = pygame.image.load(path_tube).convert_alpha()
        # Loading items start position.
        self.ether_pos = self.level.start
        self.tube_pos = self.level.start
        self.needle_pos = self.level.start
        # list random items position:
        self.list_pos = []
        # item counter:
        self.counter = 0

    def generate_items_position(self):
        """method that generates 3 random positions for displaying objects."""
        while len(self.list_pos) != 3:
            self.list_pos = random.sample(self.level.paths, 3)
            for pos in self.list_pos:
                if pos == self.level.start:
                    self.list_pos = []
                elif pos == self.level.exit:
                    self.list_pos == []
        self.ether_pos = self.list_pos[0]
        self.needle_pos = self.list_pos[1]
        self.tube_pos = self.list_pos[2]

    def render_ether(self):
        """displays the object: ether."""
        self.screen.blit(self.ether, self.ether_pos)

    def render_needle(self):
        """displays the object: needle."""
        self.screen.blit(self.needle, self.needle_pos)

    def render_tube(self):
        """displays the object: tube."""
        self.screen.blit(self.tube, self.tube_pos)

    def render_syringe(self):
        """displays the object: syringe."""
        self.screen.blit(self.syringe, (200, 650))

    def pick_up(self):
        """controls the position of the hero on the object,
            increments the assigned self.counter and
            gives a new position to objects"""
        if self.hero.position == self.ether_pos:
            self.ether_pos = (50, 650)
            self.counter += 1
        elif self.hero.position == self.tube_pos:
            self.tube_pos = (100, 650)
            self.counter += 1
        elif self.hero.position == self.needle_pos:
            self.needle_pos = (150, 650)
            self.counter += 1
