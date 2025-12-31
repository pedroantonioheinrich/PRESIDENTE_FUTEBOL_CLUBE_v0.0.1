import time
import json
import os
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json




def entrepreneur_menu():
    utils.clear_screen()

    print(f"\n{color('GREEN')}┌" + "─"*73 + "┐")
    print(f"│{color('BOLD')}{color('GREEN')}  🚀 O SONHO DO MADE MAN {' ':^47} {color('RESET')}{color('GREEN')}│")
    print(f"│{color('GREEN')}  📊 SUOR, CÁLCULO & GLÓRIA {' ':^44} {color('RESET')}{color('GREEN')}│")
    print(f"└" + "─"*73 + f"┘{color('RESET')}")

    print(f"{color('CYAN')}╔" + "═"*75 + "╗")
    print(f"║{color('BOLD')}{' 📑 O PLANO DE NEGÓCIOS ':^74}{color('RESET')}{color('CYAN')}║")
    print(f"╠" + "═"*75 + "╣")
    narrativa = [
        "O escritório é pequeno, o café é amargo e o telefone não para de tocar.",
        "Você vendeu sua última startup para perseguir um sonho: o futebol.",
        "",
        "Cada centavo foi suado. Você não tem o nome da elite, mas tem os números.",
        "A torcida te olha com desconfiança, mas os investidores te respeitam.",
        "Você começará por baixo, mas o império que construir será SEU."
    ]
    for linha in narrativa:
        print(f"║  {linha:<73}║")
    
    print(f"╚" + "═"*75 + f"╝{color('RESET')}")

    # Status Financeiro
    print(f"\n{color('YELLOW')}💸 CAPITAL INICIAL DISPONÍVEL: {color('GREEN')}$ 5.000.000,00{color('RESET')}")
    print(f"{color('BOLD')}📈 BÔNUS DE GESTÃO: {color('CYAN')}+10% EM DIVIDENDOS{color('RESET')}")
            
    print(f"\n{color('MAGENTA')}Digite [1] para assinar seu primeiro contrato...{color('RESET')}")
    print(f"{color('MAGENTA')}Digite [0] para voltar ao menu anterior: {color('RESET')}")
        
    choice = input()
        
    if choice == '0':
        from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_menu import display_career_menu
        display_career_menu()
            
    elif choice == '1':
        print(f"\n{color('GREEN')}🖋️  Registrando firma e abrindo conta bancária...{color('RESET')}")
        # Atualiza o montante e define a escolha de carreira no JSON
        update_json('total_amount', '5000000')
        update_json('career_choice', 'entrepreneur')
        time.sleep(3)
        from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_personality import show_personality_menu
        show_personality_menu()
    else:
        print(f"{color('RED')}Por favor, insira um número válido!{color('RESET')}")
        time.sleep(1)
        entrepreneur_menu()