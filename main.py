import sys
import time
from SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_menu import display_starting_menu
import SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_loading as loading_screen

class RunGame:
    def __init__(self):
        # Referenciando as funções importadas
        self.start_menu = display_starting_menu
        self.loading = loading_screen

    def run(self):
        # RunGame().loading() <<--- Ative quando quiser a barra de carregamento
        self.start_menu()

if __name__ == "__main__":
    try:
        # Inicia a instância do jogo
        game = RunGame()
        game.run()

    except KeyboardInterrupt:
        print("\n[!] Jogo interrompido pelo usuário. Saindo...")
        time.sleep(1)
        sys.exit()
    except Exception as e:
        print(f"\n[!] Erro crítico ao iniciar o jogo: {e}")
        sys.exit()
