import pygame, sys
import pygame.locals as const
from constants import *
from map import Map
from hero import Hero
from items import Item
from popup import Popup


def main():

    pygame.init()
    screen_windows = pygame.display.set_mode(resolution)
    pygame.display.set_caption("Escape Game")

    # Loading home image:
    home = pygame.image.load(path_home).convert_alpha()
    # Loading Game_over image:
    game_over = pygame.image.load(path_game_over).convert_alpha()
    # Loading Congrats image:
    congrats = pygame.image.load(path_congrats).convert()

    # Main loop:
    main_loop = True
    while main_loop:

        pygame.time.Clock().tick(30)
        menu_loop = True
        while menu_loop:

            pygame.time.Clock().tick(30)
            for event in pygame.event.get():
                if event.type == const.QUIT:
                    sys.exit()
                if (event.type == const.KEYDOWN and
                        event.key == const.K_RETURN):
                    menu_loop = False
            screen_windows.blit(home, (0, 0))
            pygame.display.flip()

        # Loading background:
        backg = pygame.image.load(path_bg).convert()

        # Loading level:
        level = Map(screen_windows)
        level.import_map()

        # Loading hero:
        mac = Hero(screen_windows, level)

        # Loading items on the map:
        items = Item(screen_windows, level, mac)
        items.generate_items_position()

        # Loading popup:
        pop_up = Popup(screen_windows, mac, items)

        game_loop = True
        while game_loop:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == const.QUIT:
                    sys.exit()
                elif (event.type == const.KEYDOWN and
                        event.key == const.K_ESCAPE):
                    game_loop = 0
                else:
                    mac.get_event(event)

            # Loading all elements of maze:
            screen_windows.blit(backg, (0, 0))
            items.render_ether()
            items.render_needle()
            items.render_tube()
            pop_up.render_message()
            level.generate()
            pop_up.render_message()

            items.pick_up()
            mac.render()
            pop_up.renderPopUp(mac.position)

            # Condition to display the image of the syringe.
            if items.counter == 3:
                items.render_syringe()
            # Condition to exit.
            if mac.position == level.exit and items.counter == 3:
                screen_windows.blit(congrats, (0, 0))
                game_loop = False
                main_loop = False
            elif mac.position == level.exit and items.counter != 3:
                screen_windows.blit(game_over, (0, 0))

            pygame.display.flip()
    # Wait 5 sec before close the screen_windows.
    pygame.time.wait(5000)

if __name__ == "__main__":
    main()