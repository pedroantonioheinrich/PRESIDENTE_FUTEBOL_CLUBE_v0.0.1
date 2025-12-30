import time
import json
import os
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete

class CareerHeir:
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.show_story()

    def show_story(self):
        last_name = self.load_family_name().upper()
        utils.clear_screen()
        print(f"\n{self.color('CIANO')}┌" + "─"*73 + "┐")
        print(f"│{self.color('BOLD')}{self.color('GOLD')}  👑 O LEGADO DOS {last_name:<54} {self.color('RESET')}{self.color('CIANO')}│")
        print(f"│{self.color('GOLD')}  💰 FORTUNA & TRADIÇÃO {' ':^48} {self.color('RESET')}{self.color('CIANO')}│")
        print(f"└" + "─"*73 + f"┘{self.color('RESET')}")

        # Texto Narrativo
        print(f"{self.color('CIANO')}╔" + "═"*75 + "╗")
        print(f"║{self.color('BOLD')}{' O TESTAMENTO DE OURO ':^75}{self.color('RESET')}{self.color('CIANO')}║")
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
        print(f"╚" + "═"*75 + f"╝{self.color('RESET')}")

        print(f"\n{self.color('AMARELO')}💰 CAPITAL INICIAL LIBERADO: {self.color('GREEN')}$ 500.000.000,00{self.color('RESET')}")
        print(f"{self.color('BOLD')}⚠️ STATUS DE PRESSÃO: {self.color('RED')}EXTREMO{self.color('RESET')}")
        
        print(f"\n{self.color('MAGENTA')}Digite [1] para reivindicar seu direito de nascença...{self.color('RESET')}")
        print(f"{self.color("MAGENTA")}Digite [0], para voltar ao menu anterior: {self.color("RESET")}")
        choice = input()
        if choice == '0':
            from SRC.USER_INTERFACE.CAREER_CHOICE.career_choice_menu import CareerChoice
            CareerChoice()
        elif choice == '1':
            print(f"{self.color("GREEN")}Reivindicando seu império...{self.color("RESET")}")
            time.sleep(1)
        else:
            print(f"{self.color("RED")}Por favor, insira um número válido!{self.color("RESET")}")
            time.sleep(1)
        
    def load_family_name(self):
        # Carregar o nome da família do arquivo de salvamento
        try:
            with open('SAVES/user_data.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                family_name = data.get('lastname', 'DESCONHECIDO').upper()
                return family_name
        except FileNotFoundError:
            return 'DESCONHECIDO'