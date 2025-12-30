import os 
import time
import sys
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete
from SRC.USER_INTERFACE.CAREER_CHOICE.career_choice_menu import CareerChoice
from SRC.USER_INTERFACE.USER_REGISTRATION.user_registration import UserRegistration




class StartMenu:
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.display_starting_menu()           
    
    
    def display_starting_menu(self):
            os.system('cls' if os.name == 'nt' else 'clear')
            # Arte ASCII principal - Nome do Jogo
            print(f"{self.color("GOLDEN")}")
            print(r"  ____  ____  _____ ____ ___ ____  _____ _   _ _____ _____    ____   ____      ")
            print(r" |  _ \|  _ \| ____/ ___|_ _|  _ \| ____| \ | |_   _| ____| |  ___|/  ___|     ")
            print(r" | |_) | |_) |  _| \___ \| || | | |  _| |  \| | | | |  _|   | |_  |  |         ")
            print(r" |  __/|  _ <| |___ ___) | || |_| | |___| |\  | | | | |___  |  _| |  |___  __ ")
            print(r" |_|   |_| \_\_____|____/___|____/|_____|_| \_| |_| |_____| |_|    \ ____||__|")
            print(r"                                                                               ")
            print(f"{self.color("RESET")}")
            
            # Informações do Sistema
            print(f"{self.color("CIANO")}╔" + "═"*75 + "╗")
            print(f"║{self.color("BOLD")}{self.color("BRANCO")}{'PRESIDENTE FUTEBOL CLUBE 2025':^75}{self.color("RESET")}{self.color("CIANO")}║")
            print(f"║{'SISTEMA PROFISSIONAL DE GESTÃO ESPORTIVA':^75}║")
            print(f"╚" + "═"*75 + f"╝{self.color("RESET")}")
            
            # Créditos - Pedro Antônio Heinrich
            print(f" {self.color("AMARELO")}Desenvolvido por:{self.color("RESET")} {self.color("MAGENTA")}Pedro Antônio Heinrich{self.color("RESET")} {self.color("SILVER")}@streetegist{self.color("RESET")}".center(85))
            print(f"{self.color("CIANO")}" + "-" * 77 + f"{self.color("RESET")}")      
            # Menu de Opções
            print(f"\n {self.color("YELLOW")}[1]{self.color("RESET")} {self.color("BOLD")}🚀 INICIAR NOVA CARREIRA{self.color("RESET")}")
            print(f" {self.color("YELLOW")}[2]{self.color("RESET")} {self.color("BOLD")}📂 CARREGAR CARREIRA EXISTENTE (SLOTS){self.color("RESET")}")
            print(f" {self.color("YELLOW")}[3]{self.color("RESET")} {self.color("BOLD")}⚙️ CONFIGURAÇÕES E OPÇÕES{self.color("RESET")}")
            print(f" {self.color("RED")}[0]{self.color("RESET")} {self.color("BOLD")} ENCERRAR SIMULADOR{self.color("RESET")}\n")

            choice = input(f"{self.color("MAGENTA")}Selecione uma opção [1-3] ou [0] para sair: {self.color("RESET")}")

            match(choice):
                case '1':
                    print(f"{self.color("GREEN")}Começando uma nova carreira...{self.color("RESET")}")
                    time.sleep(1)
                    UserRegistration()
                    

                case '2':
                    print(f"{self.color("GREEN")}Carregando carreira...{self.color("RESET")}")
                    time.sleep(1)
                case '3':
                    print(f"{self.color("GREEN")}Abrindo menu de opções...{self.color("RESET")}")
                    time.sleep(1)
                case '0':
                    print(f"{self.color("RED")}Saindo do jogo. Tchau!{self.color("RESET")}")
                    time.sleep(1)
                    sys.exit()
                case _:
                    print(f"{self.color("RED")}Por favor, insira um número válido!{self.color("RESET")}")
                    time.sleep(1)
                    self.display_starting_menu()    



