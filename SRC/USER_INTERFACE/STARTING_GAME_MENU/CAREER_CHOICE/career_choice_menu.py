import time
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json


def display_career_menu():

    utils.clear_screen()

    # Cabeçalho de Seleção
    print(f"{color('GOLDEN')}╔" + "═"*73 + "╗")
    print(f"║{color('RESET')}{color('BOLD')}  💎 PATRIMÔNIO INICIAL & ASCENSÃO{' ':^39}{color('GOLDEN')}║")
    print(f"╠" + "═"*73 + "╣")
    print(f"║{color('RESET')}  {color('GOLDEN')}✨ ORIGEM DA SUA FORTUNA: {color('BOLD')}Como você construiu seu império?{color('RESET')}{' ':^13}{color('GOLDEN')}║")
    print(f"╚" + "═"*73 + f"╝{color('RESET')}")
    # Herdeiro
    print(f"{color('CIANO')}╔" + "═"*75 + "╗")
    print(f"║ {color('GOLDEN')}{color('BOLD')} [1] O HERDEIRO (Nível: Fácil / Narrativo) {' ':^31}{color('RESET')}{color('CIANO')}║")
    print(f"║  - Capital Inicial: $$$$$ (Fortuna Incalculável) {' ':25}║")
    print(f"║  - Vantagem: Pode comprar SAFs ou fundar clubes no dia 1. {' ':16}║")
    print(f"║  - Risco: Alta pressão por resultados. Perda rápida de apoio político. {' ':3}║")
    print(f"╚" + "═"*75 + f"╝{color('RESET')}")

    print("\n" + " " * 35 + f"{color('SILVER')}OU{color('RESET')}" + "\n")

    # Empresário
    print(f"{color('CIANO')}╔" + "═"*75 + "╗")
    print(f"║ {color('GREEN')}{color('BOLD')} [2] O EMPRESÁRIO (Nível: Médio / Gestão) {' ':32}{color('RESET')}{color('CIANO')}║")
    print(f"║  - Capital Inicial: $ (Investimento Próprio) {' ':29}║")
    print(f"║  - Vantagem: Maior rendimento de dividendos e bônus de gestão. {' ':11}║")
    print(f"║  - Risco: Precisa de tempo para acumular capital e apoio popular. {' ':8}║")
    print(f"╚" + "═"*75 + f"╝{color('RESET')}")

    choice = input(f"\n{color('MAGENTA')}Como sua história começa? Selecione [1-2] ou [0] Voltar: {color('RESET')}")

    match(choice):
        case '1':
            print(f"\n{color('GOLDEN')}✨ Escolha clássica! Preparando o berço de ouro e o champanhe...{color('RESET')}")
            print(f"{color('SILVER')}💭 'Obrigado, vovô! Prometo não gastar tudo em uma semana.'{color('RESET')}")
            update_json('career_choice', 'heir')
            time.sleep(2)
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_heir import heir_menu
            heir_menu()
            
        case '2':
            print(f"\n{color('GREEN')}📈 Visão de mercado! Onde os outros veem grama, você vê lucro.{color('RESET')}")
            print(f"{color('SILVER')}💭 'Café amargo e planilhas no Excel... a glória está chegando.'{color('RESET')}")
            update_json('career_choice', 'entrepreneur')
            # Note que no código anterior você usou 5.000.000, ajuste conforme seu balanceamento
            update_json('total_amount', '5000000') 
            time.sleep(2)
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_entrepreneur import entrepreneur_menu
            entrepreneur_menu()
            
        case '0':
            print(f"\n{color('CIANO')}🔙 Recuando para a defesa... voltando ao menu principal.{color('RESET')}")
            time.sleep(1)
            from SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_menu import display_starting_menu
            display_starting_menu()
            
        case _:
            print(f"\n{color('RED')}🚫 Erro no VAR! Essa opção não existe. Tente novamente.{color('RESET')}")
            time.sleep(1.5)
            display_career_menu() # Recarrega o menu para o usuário tentar de novo

