import sys
import time
from SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_menu import StartMenu
import SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_loading as loading_module

class RunGame:
    def __init__(self):
        self.start_menu = StartMenu
        self.loading = loading_module.loading_screen


if __name__ == "__main__":
    try:
        RunGame().loading()
        RunGame().start_menu()
     
    except KeyboardInterrupt:
        print("Game interrupted by user. Exiting...")
        time.sleep(1)
        sys.exit()  
