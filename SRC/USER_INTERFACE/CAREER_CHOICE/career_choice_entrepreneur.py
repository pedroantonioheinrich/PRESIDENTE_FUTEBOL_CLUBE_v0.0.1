import time
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete

class CareerEntrepreneur:
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.show_story()

    def show_story(self):
        utils.clear_screen()
        print(f"{self.color('GREEN')}")
        print(r"      __________                                 ")
        print(r"     |  ______  |    O SONHO DO      _______     ")
        print(r"     | |      | |    ENTREPRENEUR   |_______|    ")
        print(r"     | |______| |                                ")
        print(r"     |  ______  |    SUOR, CÁLCULO & GLÓRIA      ")
        print(r"     |_|      |_|                                ")
        print(f"{self.color('RESET')}")

        # Texto Narrativo
        print(f"{self.color('CIANO')}╔" + "═"*75 + "╗")
        print(f"║{self.color('BOLD')}{' O PLANO DE NEGÓCIOS ':^75}{self.color('RESET')}{self.color('CIANO')}║")
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
        print(f"╚" + "═"*75 + f"╝{self.color('RESET')}")

        print(f"\n{self.color('AMARELO')}💸 CAPITAL INICIAL DISPONÍVEL: {self.color('GREEN')}$ 5.000.000,00{self.color('RESET')}")
        print(f"{self.color('BOLD')}📈 BÔNUS DE GESTÃO: {self.color('CIANO')}+10% EM DIVIDENDOS{self.color('RESET')}")
        
        input(f"\n{self.color('MAGENTA')}Pressione ENTER para assinar seu primeiro contrato...{self.color('RESET')}")