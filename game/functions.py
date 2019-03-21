import os
"""two functions to create paths to "sprites" and "levels" folders"""


def path_to_level(name):
    path = os.path.join(os.path.dirname(__file__), "levels\\{}".format(name))
    return path


def path_to_image(name):
    path = os.path.join(os.path.dirname(__file__), "sprites\\{}".format(name))
    return path
