import time
import json
import os
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json





def heir_menu():
    last_name = load_family_name().upper()
    utils.clear_screen()
    print(f"\n{color('CIANO')}┌" + "─"*73 + "┐")
    print(f"│{color('BOLD')}{color('GOLD')}  👑 O LEGADO DOS {last_name:<54} {color('RESET')}{color('CIANO')}│")
    print(f"│{color('GOLD')}  💰 FORTUNA & TRADIÇÃO {' ':^48} {color('RESET')}{color('CIANO')}│")
    print(f"└" + "─"*73 + f"┘{color('RESET')}")


    print(f"{color('CIANO')}╔" + "═"*75 + "╗")
    print(f"║{color('BOLD')}{' O TESTAMENTO DE OURO ':^75}{color('RESET')}{color('CIANO')}║")
    print(f"╠" + "═"*75 + "╣")
    narrativa = [
    "Você abre o envelope lacrado com o brasão da família. Dentro, a notícia:",
    "Seu avô, um magnata do aço, deixou um império sob seus cuidados.",
    "",
    "O dinheiro nunca foi um problema, mas o sobrenome carrega um peso enorme.",
    "As manchetes já dizem: 'O herdeiro assumirá o controle do futebol?'.",
    "Sua conta bancária transborda, mas sua paciência política será testada."
    ]
    for linha in narrativa:
        print(f"║  {linha:<73}║")
        print(f"╚" + "═"*75 + f"╝{color('RESET')}")

        print(f"\n{color('AMARELO')}💰 CAPITAL INICIAL LIBERADO: {color('GREEN')}$ 500.000.000,00{color('RESET')}")
        print(f"{color('BOLD')}⚠️ STATUS DE PRESSÃO: {color('RED')}EXTREMO{color('RESET')}")
        
        print(f"\n{color('MAGENTA')}Digite [1] para reivindicar seu direito de nascença...{color('RESET')}")
        print(f"{color("MAGENTA")}Digite [0], para voltar ao menu anterior: {color("RESET")}")
        choice = input()
        if choice == '0':
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_menu import display_career_menu
            display_career_menu()
        
        elif choice == '1':
            print(f"{color("GREEN")}💰 💰 Reivindicando seu império...{color("RESET")}")
            update_json('total_amount', '500000000')
            time.sleep(3)
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_personality import show_personality_menu
            show_personality_menu()

        else:
            print(f"{color("RED")}Por favor, insira um número válido!{color("RESET")}")
            time.sleep(1)
            heir_menu()
        
def load_family_name():
# Carregar o nome da família do arquivo de salvamento
    try:
        with open('SAVES/user_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            family_name = data.get('lastname', 'DESCONHECIDO').upper()
            return family_name
    except FileNotFoundError:
        return 'DESCONHECIDO'