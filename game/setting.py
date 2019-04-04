""" file of game constants"""
import os.path
import pygame

# config:

settings = {
    "resolution": (750, 750),
    "sprite": 50,
    'sprite_max': 750,
    "start": (50, 50),
    # path base
    "base": os.path.dirname(__file__),
    # test
    "paths": {
        "levels": os.path.abspath(r"levels"),
        "sprites": os.path.abspath(r"sprites")
            }
    }

# path to level:
path_level = os.path.join(settings["paths"]["levels"], "level1.txt")
# path to sprites:
path_backg = os.path.join(settings["paths"]["sprites"], "backg.jpg")
path_bubble = os.path.join(settings["paths"]["sprites"], "bubble.png")
path_congrats = os.path.join(settings["paths"]["sprites"], "congrats.jpg")
path_ether = os.path.join(settings["paths"]["sprites"], "ether.png")
path_excla = os.path.join(settings["paths"]["sprites"], "excla.png")
path_game_over = os.path.join(settings["paths"]["sprites"], "g_o.png")
path_guardian = os.path.join(settings["paths"]["sprites"], "guardian.png")
path_home = os.path.join(settings["paths"]["sprites"], "home.png")
path_inter = os.path.join(settings["paths"]["sprites"], "inter.png")
path_mac = os.path.join(settings["paths"]["sprites"], "mac.png")
path_needle = os.path.join(settings["paths"]["sprites"], "needle.png")
path_syringe = os.path.join(settings["paths"]["sprites"], "syringe.png")
path_tube = os.path.join(settings["paths"]["sprites"], "tube.png")
path_wall = os.path.join(settings["paths"]["sprites"], "wall.png")

# Directions:
d_top = -settings["sprite"]
d_bottom = settings["sprite"]
d_right = settings["sprite"]
d_left = -settings["sprite"]

# bubble position
bubble_pos = ((settings["start"][0] + 40), (settings["start"][1] + 40))
