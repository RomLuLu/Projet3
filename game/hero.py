import pygame
import pygame.locals as const
from constants import *


class Hero:

    def __init__(self, screen, level):
        self.screen = screen
        self.level = level
        self.mac = pygame.image.load(path_mac).convert_alpha()
        # hero start position.
        self.position = start

    def render(self):
        """Displays the image of the hero at the desired position."""
        self.screen.blit(self.mac, self.position)

    def set_position(self, direction):
        """calculates the position of the hero according to
            the key recorded by the player."""
        new_position = self.position
        if direction == 'TOP':
            new_position = new_position[0], new_position[1] + d_top
        elif direction == 'BOTTOM':
            new_position = new_position[0], new_position[1] + d_bottom
        elif direction == 'RIGHT':
            new_position = new_position[0] + d_right, new_position[1]
        elif direction == 'LEFT':
            new_position = new_position[0] + d_left, new_position[1]
        if new_position in self.level.paths:
            self.position = new_position

    def get_event(self, event):
        """method that controls the keys used by the player."""
        if (event.type == const.KEYDOWN and
                event.key == const.K_UP):
            self.set_position('TOP')
        elif (event.type == const.KEYDOWN and
                event.key == const.K_DOWN):
            self.set_position('BOTTOM')
        elif (event.type == const.KEYDOWN and
                event.key == const.K_RIGHT):
            self.set_position('RIGHT')
        elif (event.type == const.KEYDOWN and
                event.key == const.K_LEFT):
            self.set_position('LEFT')
