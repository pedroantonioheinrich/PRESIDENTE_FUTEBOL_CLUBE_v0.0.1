import time
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json

class CareerChoice:
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.display_career_menu()

    def display_career_menu(self):
        utils.clear_screen()
        
        # Cabeçalho de Seleção
        print(f"{self.color('GOLDEN')}╔" + "═"*73 + "╗")
        print(f"║{self.color('RESET')}{self.color('BOLD')}  💎 PATRIMÔNIO INICIAL & ASCENSÃO{' ':^39}{self.color('GOLDEN')}║")
        print(f"╠" + "═"*73 + "╣")
        print(f"║{self.color('RESET')}  {self.color('GOLDEN')}✨ ORIGEM DA SUA FORTUNA: {self.color('BOLD')}Como você construiu seu império?{self.color('RESET')}{' ':^13}{self.color('GOLDEN')}║")
        print(f"╚" + "═"*73 + f"╝{self.color('RESET')}")
        # Herdeiro
        print(f"{self.color('CIANO')}╔" + "═"*75 + "╗")
        print(f"║ {self.color('GOLDEN')}{self.color('BOLD')} [1] O HERDEIRO (Nível: Fácil / Narrativo) {' ':^31}{self.color('RESET')}{self.color('CIANO')}║")
        print(f"║  - Capital Inicial: $$$$$ (Fortuna Incalculável) {' ':25}║")
        print(f"║  - Vantagem: Pode comprar SAFs ou fundar clubes no dia 1. {' ':16}║")
        print(f"║  - Risco: Alta pressão por resultados. Perda rápida de apoio político. {' ':3}║")
        print(f"╚" + "═"*75 + f"╝{self.color('RESET')}")

        print("\n" + " " * 35 + f"{self.color('SILVER')}OU{self.color('RESET')}" + "\n")

        # Empresário
        print(f"{self.color('CIANO')}╔" + "═"*75 + "╗")
        print(f"║ {self.color('GREEN')}{self.color('BOLD')} [2] O EMPRESÁRIO (Nível: Médio / Gestão) {' ':32}{self.color('RESET')}{self.color('CIANO')}║")
        print(f"║  - Capital Inicial: $ (Investimento Próprio) {' ':29}║")
        print(f"║  - Vantagem: Maior rendimento de dividendos e bônus de gestão. {' ':11}║")
        print(f"║  - Risco: Precisa de tempo para acumular capital e apoio popular. {' ':8}║")
        print(f"╚" + "═"*75 + f"╝{self.color('RESET')}")
        
        choice = input(f"\n{self.color('MAGENTA')}Como sua história começa? Selecione [1-2] ou [0] Voltar: {self.color('RESET')}")

        

        match(choice):
            case '1':
                update_json('career_choice', 'heir')
                time.sleep(2)
                from SRC.USER_INTERFACE.CAREER_CHOICE.career_choice_heir import CareerHeir
                CareerHeir()
            case '2':
                update_json('career_choice', 'entrepreneur')
                time.sleep(2)
                from SRC.USER_INTERFACE.CAREER_CHOICE.career_choice_entrepreneur import CareerEntrepreneur
                CareerEntrepreneur()
            case '0':
                from SRC.USER_INTERFACE.STARTING_GAME_MENU.starting_game_menu import StartMenu
                StartMenu()   

        return choice