import time
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete

class UserPersonality:
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.personality_data = None
        self.display_options()

    def display_options(self):
        utils.clear_screen()
        
        # Cabeçalho Minimalista Seguindo o seu padrão
        print(f"{self.color('CIANO')}┌" + "─"*73 + "┐")
        print(f"│ {self.color('BOLD')}PERFIL DE LIDERANÇA EXECUTIVA{' ':^42}{self.color('RESET')}{self.color('CIANO')}│")
        print(f"└" + "─"*73 + f"┘{self.color('RESET')}")
        
        print(f"\n {self.color('SILVER')}Defina como você será conhecido nos bastidores do futebol:{self.color('RESET')}\n")

        # Opção 1
        print(f" {self.color('RED')}[1] O CENTRALIZADOR{self.color('RESET')}")
        print(f"     {self.color('SILVER')}Bônus: +15% Respeito do Vestiário | Risco: -10% Apoio da Diretoria{self.color('RESET')}\n")

        # Opção 2
        print(f" {self.color('GREEN')}[2] O DIPLOMATA{self.color('RESET')}")
        print(f"     {self.color('SILVER')}Bônus: +10% Sucesso em Negociações | Risco: Dificuldade em Punir Atletas{self.color('RESET')}\n")

        # Opção 3
        print(f" {self.color('YELLOW')}[3] O ESTRATEGISTA{self.color('RESET')}")
        print(f"     {self.color('SILVER')}Bônus: Visão de Atributos Ocultos | Risco: Torcida exige resultados imediatos{self.color('RESET')}\n")

        print(f"{self.color('CIANO')}" + "─" * 75 + f"{self.color('RESET')}")
        
        choice = input(f" {self.color('MAGENTA')}➤ SELECIONE SEU PERFIL (1-3): {self.color('RESET')}").strip()

        match choice:
            case '1':
                self.personality_data = "Centralizador"
            case '2':
                self.personality_data = "Diplomata"
            case '3':
                self.personality_data = "Estrategista"
            case _:
                print(f"\n {self.color('RED')}⚠️ Opção inválida! Escolha entre 1, 2 ou 3.{self.color('RESET')}")
                time.sleep(1.5)
                self.display_options()

        self.confirmation()
        return self.personality_data

    def confirmation(self):
        print(f"\n{self.color('CIANO')}" + "─" * 75 + f"{self.color('RESET')}")
        print(f" {self.color('GREEN')}Perfil definido: O {self.personality_data} está pronto para assumir o cargo.{self.color('RESET')}")
        time.sleep(1.5)