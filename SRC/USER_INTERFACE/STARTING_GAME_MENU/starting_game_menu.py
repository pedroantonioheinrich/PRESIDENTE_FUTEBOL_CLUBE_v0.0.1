import os 
import time
import sys
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color


def display_starting_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Arte ASCII principal - Nome do Jogo
    print(f"{color("GOLDEN")}")
    print(r"  ____  ____  _____ ____ ___ ____  _____ _   _ _____ _____    ____   ____      ")
    print(r" |  _ \|  _ \| ____/ ___|_ _|  _ \| ____| \ | |_   _| ____| |  ___|/  ___|     ")
    print(r" | |_) | |_) |  _| \___ \| || | | |  _| |  \| | | | |  _|   | |_  |  | ")
    print(r" |  __/|  _ <| |___ ___) | || |_| | |___| |\  | | | | |___  |  _| |  |___  __ ")
    print(r" |_|   |_| \_\_____|____/___|____/|_____|_| \_| |_| |_____| |_|    \ ____||__|")
    print(r"       ")
    print(f"{color("RESET")}")
    
    # Informações do Sistema
    print(f"{color("CIANO")}╔" + "═"*75 + "╗")
    print(f"║{color("BOLD")}{color("BRANCO")}{'PRESIDENTE FUTEBOL CLUBE 2025':^75}{color("RESET")}{color("CIANO")}║")
    print(f"║{'SISTEMA PROFISSIONAL DE GESTÃO ESPORTIVA':^75}║")
    print(f"╚" + "═"*75 + f"╝{color("RESET")}")
    
    # Créditos - Pedro Antônio Heinrich
    print(f" {color("AMARELO")}Desenvolvido por:color{("RESET")} {color("MAGENTA")}Pedro Antônio Heinrich{color("RESET")} {color("SILVER")}@streetegistcolor{color("RESET")}".center(85))
    print(f"{color("CIANO")}" + "-" * 77 + f"{color("RESET")}")      
    # Menu de Opções
    print(f"\n {color("YELLOW")}[1]{color("RESET")} {color("BOLD")}🚀 INICIAR NOVA CARREIRA{color("RESET")}")
    print(f" {color("YELLOW")}[2]{color("RESET")} {color("BOLD")}📂 CARREGAR CARREIRA EXISTENTE (SLOTS){color("RESET")}")
    print(f" {color("YELLOW")}[3]{color("RESET")} {color("BOLD")}⚙️ CONFIGURAÇÕES E OPÇÕES{color("RESET")}")
    print(f" {color("RED")}[0]{color("RESET")} {color("BOLD")} ENCERRAR SIMULADOR{color("RESET")}\n")

    choice = input(f"{color("MAGENTA")}Selecione uma opção [1-3] ou [0] para sair: {color("RESET")}")

    match(choice):
        case '1':
            print(f"{color("GREEN")}Começando uma nova carreira...{color("RESET")}")
            time.sleep(1)
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.USER_REGISTRATION.user_registration import user_registration
            user_registration()
        case '2':
            print(f"{color("GREEN")}Carregando carreira...{color("RESET")}")
            time.sleep(1)
        case '3':
            print(f"{color("GREEN")}Abrindo menu de opções...{color("RESET")}")
            time.sleep(1)
        case '0':
            print(f"{color("RED")}Saindo do jogo. Tchau!{color("RESET")}")
            time.sleep(1)
            sys.exit()
        case _:
            print(f"{color("RED")}Por favor, insira um número válido!{color("RESET")}")
            time.sleep(1)
            display_starting_menu()    



