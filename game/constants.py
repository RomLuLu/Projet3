""" file of game constants"""
from functions import *
import pygame

# screen resolution:
resolution = (750, 750)

# size sprites in pixel:
sprite = 50 
sprite_max = 750

# start position:
start = (50, 50)

# link to the pass images:
path_home = path_to_image("acceuil.png")
path_needle = path_to_image("aiguille.png")
path_ether = path_to_image("ether.png")
path_bg = path_to_image("font.jpg")
path_guardian = path_to_image("Gardien.png")
path_mac = path_to_image("MacGyver.png")
path_syringe = path_to_image("seringue.png")
path_tube = path_to_image("tube_plastique.png")
path_wall = path_to_image("wall.png")
path_game_over = path_to_image("game_over.png")
path_congrats = path_to_image("congrarulations.jpg")
path_inter = path_to_image("interrogation.png")
path_excla = path_to_image("exclamation.png")
path_bubble = path_to_image("bubble.png")

# Directions:
d_top = -sprite
d_bottom = sprite
d_right = sprite
d_left = -sprite

# bubble position
bubble_pos = ((start[0] + 40), (start[1] + 40))