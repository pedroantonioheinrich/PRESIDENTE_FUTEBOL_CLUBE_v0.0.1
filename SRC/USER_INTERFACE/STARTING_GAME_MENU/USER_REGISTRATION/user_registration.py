import time
import json
import os
import random
import datetime as dt
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils_json_update import save_json

# Variáveis globais limpas
day = None 
month = None 
year = None 
name = None  
lastname = None
user_data = {}

def id_serializer():
    unique_id = random.randint(100000, 999999)
    timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{timestamp}-{unique_id}"

def user_registration():
    global day, month, year, name, lastname, user_data

    utils.clear_screen()
            
    # Cabeçalho
    print(f"{color('CIANO')}┌" + "─"*73 + "┐")
    print(f"│ {color('BOLD')}📋 CADASTRO DE CREDENCIAIS: {color('GOLD')}FUTURO PRESIDENTE{color('RESET')}{' ':^27}{color('CIANO')}│")
    print(f"├" + "─"*73 + "┤")
    print(f"│ {color('BOLD')}⚽ Comece a escrever sua história no mundo do futebol...{' ':^16}{color('RESET')}{color('CIANO')}│")
    print(f"└" + "─"*73 + f"┘{color('RESET')}")

    print(f"\n{color('CIANO')}   " + "─" * 69 + f"{color('RESET')}")

    # Gerar ID único
    user_data['user_id'] = id_serializer()
            
    # Input de Nome
    while True:
        name = input(f"\n {color('YELLOW')}➤ NOME:{color('RESET')} ").strip().title()
        if name:
            break
        print(f"{color('RED')} Por favor, insira um nome válido! {color('RESET')}")

    # Input de Sobrenome
    while True:
        lastname = input(f" {color('YELLOW')}➤ SOBRENOME:{color('RESET')} ").strip().title()
        if lastname:
            break
        print(f"{color('RED')} Por favor, insira um sobrenome válido! {color('RESET')}")

    user_data['name'] = name
    user_data['lastname'] = lastname
    
    print(f"\n{color('CIANO')}" + "─" * 75 + f"{color('RESET')}")
    print(f" {color('YELLOW')}➤ DATA DE NASCIMENTO:{color('RESET')}")

    # Validação de Data com While para evitar recursão infinita
    while True:
        day_in = input(" Dia (DD): ")
        if day_in.isdigit() and 1 <= int(day_in) <= 31:
            day = f"{int(day_in):02d}"
            break
        print(f"{color('RED')} Dia inválido! {color('RESET')}")

    while True:
        month_in = input(" Mês (MM): ")
        if month_in.isdigit() and 1 <= int(month_in) <= 12:
            month = f"{int(month_in):02d}"
            break
        print(f"{color('RED')} Mês inválido! {color('RESET')}")

    while True:
        year_in = input(" Ano (AAAA): ")
        if year_in.isdigit() and 1900 <= int(year_in) <= 2024:
            year = str(year_in)
            break
        print(f"{color('RED')} Ano inválido! {color('RESET')}")

    user_data['birth_date'] = f"{day}/{month}/{year}"

    print(f"\n{color('CIANO')}" + "─" * 75 + f"{color('RESET')}")
    print(f" {color('YELLOW')}➤ NACIONALIDADE:{color('RESET')}")
    user_data['nationality'] = input(">    ").strip().title()

    print(f"\n{color('CIANO')}" + "─" * 75 + f"{color('RESET')}")
    print(f"{color('GREEN')} Processando credenciais...{color('RESET')}")
    time.sleep(1)
            
    # Salvamento
    save_json(user_data)
    confirmation()

def confirmation():
    # Usando as globais atualizadas
    print(f"\n{color('CYAN')}" + "─" * 75 + f"{color('RESET')}")
    print(f"{color('GREEN')} Credenciais confirmadas! Bem-vindo, {user_data['name']} {user_data['lastname']}.{color('RESET')}")
    time.sleep(1.3)
    # Import local para evitar erro circular
    from SRC.USER_INTERFACE.STARTING_GAME_MENU.CAREER_CHOICE.career_choice_menu import display_career_menu
    display_career_menu()