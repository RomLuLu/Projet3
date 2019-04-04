# Projet3

THE GAME:
    This an escape game.
    GOAL: 
    You must help MacGYver escape from prison.
    he will need to pick up 3 objects: a tube, of the ether, a needle to make a sock to lull the guard.
    The game is won when all the steps are completed otherwise MacGyver dies.

CONTENS OF THE FILE 'GAME':
    -> A 'levels' folder that contains the unique labyrinth map.
    -> A 'sprites' folder that contains the images of the game.
    -> And several '.py' files that allow the game to run:
        - hero.py : who handles macGyver moves.
        - map.py : which manage the conversion of the level and its translation in graphic format.
        - items.py : who manage the appearance of objects useful to MacGyver.
        - main.py : program execution file.
        - popup.py : to display some message and images
        - settings.py: EDIT path(relativ path) ou file "sprites" and "levels" to create your own path:
            -> settings["path"] : os.path.abspath(" your_relativ_path")
