import pygame, sys
import pygame.locals as const
from setting import *


class Map:
    """class who create the structure of tha maze"""
    def __init__(self, screen):
        # path to the level
        self.path = path_level
        # screen is a pygame.Surface:
        self.screen = screen
        # creation of different attributes
        self.structure = []  
        self.walls = []
        self.paths = []
        self.start = tuple()
        self.exit = tuple()
        # loading images wall, guardian and items:
        self.wall = pygame.image.load(path_wall).convert_alpha()
        self.guardian = pygame.image.load(path_guardian).convert_alpha()

    def import_map(self):
        """method that assigns coordinates to the different structure."""
        x, y = 0, 0
        with open(self.path, 'r') as f:
            structure = f.readlines()
        for line in structure:
            for item in line:
                self.structure.append((x, y))
                if item == 'M':
                    self.walls.append((x, y))
                elif item == 'p':
                    self.paths.append((x, y))
                elif item == 'E':
                    self.paths.append((x, y))
                    self.exit = (x, y)
                elif item == 'S':
                    self.paths.append((x, y))
                    self.start = (x, y)
                x += settings["sprite"]
            x, y = 0, y + settings["sprite"]

    def generate(self):
        """method that graphically creates the structure of the labyrinth."""
        for position in self.structure:
            if position in self.walls:
                self.screen.blit(self.wall, position)
            elif position == self.exit:
                self.screen.blit(self.guardian, position)
