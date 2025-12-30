import time
import json
import os
import random
import datetime as dt
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete
from SRC.USER_INTERFACE.CAREER_CHOICE.career_choice_menu import CareerChoice
from SRC.USER_INTERFACE.UTILS.utils_json_update import save_json

class UserRegistration:
    day = None
    month = None
    year = None
    name = None
    lastname = None
 
    def __init__(self):
        self.color_choice = ColorPallete()
        self.color = self.color_choice.color_picker
        self.user_data = {}
        self.collect_information()

    def collect_information(self):
        utils.clear_screen()
        
        # Cabeçalho
        print(f"{self.color('CIANO')}┌" + "─"*73 + "┐")
        print(f"│ {self.color('BOLD')}📋 CADASTRO DE CREDENCIAIS: {self.color('GOLD')}FUTURO PRESIDENTE{self.color('RESET')}{' ':^27}{self.color('CIANO')}│")
        print(f"├" + "─"*73 + "┤")
        print(f"│ {self.color('BOLD')}⚽ Comece a escrever sua história no mundo do futebol...{' ':^16}{self.color('RESET')}{self.color('CIANO')}│")
        print(f"└" + "─"*73 + f"┘{self.color('RESET')}")

        # Linha divisória estética antes dos inputs
        print(f"\n{self.color('CIANO')}   " + "─" * 69 + f"{self.color('RESET')}")

        # Gerar ID único para o usuário
        self.user_data['user_id'] = self.id_serializer()
        
        # Área de Input
        print(f"\n {self.color('YELLOW')}➤ NOME COMPLETO:{self.color('RESET')}")
        self.name = input(' Nome: ').strip().title()
        if(self.name == ''):
            self.name = None
            print(f"{self.color('RED')} Por favor, insira um nome válido! {self.color('RESET')}")
            time.sleep(1)
            self.collect_information()


        self.lastname = input(' Sobrenome: ').strip().title()
        if(self.lastname == ''):
            self.lastname = None
            print(f"{self.color('RED')} Por favor, insira um sobrenome válido! {self.color('RESET')}")
            time.sleep(1)
            self.collect_information()

        self.user_data['name'] = self.name
        self.user_data['lastname'] = self.lastname

        print(f"\n{self.color('CIANO')}" + "─" * 75 + f"{self.color('RESET')}")
        print(f" {self.color('YELLOW')}➤ DATA DE NASCIMENTO:{self.color('RESET')}")

        self.day = input(" Dia (DD): ")
        if(self.day.isdigit() and 1 <= int(self.day) <= 31):
            self.day = f"{int(self.day):02d}"
        else:
            self.day = None
            print(f"{self.color('RED')} Por favor, insira um dia válido! {self.color('RESET')}")
            time.sleep(1)
            self.collect_information()

        self.month = input(" Mês (MM): ")
        if(self.month.isdigit() and 1 <= int(self.month) <= 12):
            self.month = f"{int(self.month):02d}"
        else:
            self.month = None
            print(f"{self.color('RED')} Por favor, insira um mês válido! {self.color('RESET')}")    
            time.sleep(1)
            self.collect_information()

        self.year = input(" Ano (AAAA): ")
        if(self.year.isdigit() and 1900 <= int(self.year) <= 2024):
            self.year = str(self.year)
        else:
            self.year = None
            print(f"{self.color('RED')} Por favor, insira um ano válido! {self.color('RESET')}")    
            time.sleep(1)
            self.collect_information()

        self.user_data['birth_date'] = f"{self.day}/{self.month}/{self.year}"

        print(f"\n{self.color('CIANO')}" + "─" * 75 + f"{self.color('RESET')}")
        print(f" {self.color('YELLOW')}➤ NACIONALIDADE:{self.color('RESET')}")
        self.user_data['nationality'] = input(">    ").strip().title()

        

        print(f"\n{self.color('CIANO')}" + "─" * 75 + f"{self.color('RESET')}")
        print(f"{self.color('GREEN')} Processando credenciais...{self.color('RESET')}")
        time.sleep(1)
        
        if(self.day == None or self.month == None or self.year == None or
           self.name == None or self.lastname == None):
            print(f"{self.color('RED')} Por favor, preencha todos os campos corretamente! {self.color('RESET')}")
            time.sleep(1)
            self.collect_information()     
        else:
            save_json(self.user_data)
            self.confirmation()

    
    def confirmation(self):
        print(f"\n{self.color('CYAN')}" + "─" * 75 + f"{self.color('RESET')}")
        print(f"{self.color('GREEN')} Credenciais confirmadas! Bem-vindo, ao seu novo vício... {self.name} {self.lastname}.{self.color('RESET')}")
        time.sleep(1.3)
        CareerChoice().display_career_menu()

    def id_serializer(self):
        unique_id = random.randint(100000, 999999)
        timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}-{unique_id}"
