import sys
import time
from SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_menu import display_starting_menu
import SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_loading as loading_screen

class RunGame:
    def __init__(self):
        self.start_menu = display_starting_menu
        self.loading = loading_screen


if __name__ == "__main__":
    try:
        # RunGame().loading()   <<----- desativado durante fase de testes
        RunGame().start_menu()

    except KeyboardInterrupt:
        print("Jogo interrompido pelo usuario. Saindo...")
        time.sleep(1)
        sys.exit()
