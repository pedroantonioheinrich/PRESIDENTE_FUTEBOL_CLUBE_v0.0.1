import pandas as pd
import time
import json
import SRC.USER_INTERFACE.UTILS.utils as utils
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json

class ClubSelector:
    def __init__(self):
        self.csv_path = 'DATA/data_fifa_players_database.csv'
        self.user_data_path = 'SAVES/user_data.json'
        self.start_selection()

    def load_balance(self):
        try:
            with open(self.user_data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return int(data.get('total_amount', 0))
        except:
            return 0

    def start_selection(self):
        utils.clear_screen()
        balance = self.load_balance()
        
        print(f"{color('GOLDEN')}╔" + "═"*73 + "╗")
        print(f"║{color('BOLD')}  🌍 MERCADO INTERNACIONAL: ESCOLHA SUA SELEÇÃO{' ':^27}{color('GOLDEN')}║")
        print(f"║  SALDO DISPONÍVEL: {color('GREEN')}${balance:,.2f}{color('RESET')}{' ':^34}{color('GOLDEN')}║")
        print(f"╚" + "═"*73 + f"╝{color('RESET')}")

        try:
            # Carrega o CSV usando as colunas reais encontradas no seu teste
            df = pd.read_csv(self.csv_path)
            
            # No seu CSV, as colunas são: 'nationality', 'national_team' e 'overall_rating'
            col_pais = 'nationality'
            col_clube = 'national_team'
            col_rating = 'overall_rating'

            # 1. Listar Países (Nacionalidades)
            countries = sorted(df[col_pais].dropna().unique())
            print(f"\n{color('CIANO')}Selecione uma região para buscar federações:{color('RESET')}")
            
            for i, c in enumerate(countries[:15], 1):
                print(f" [{i}] {c}")
            
            c_choice = input(f"\n{color('MAGENTA')}Digite o número: {color('RESET')}")
            selected_nation = countries[int(c_choice)-1]

            # 2. Listar Seleções (Filtrando por nacionalidade)
            utils.clear_screen()
            # Filtra onde a national_team não é nula
            teams_df = df[(df[col_pais] == selected_nation) & (df[col_clube].notna())]
            teams = sorted(teams_df[col_clube].unique())
            
            if not teams:
                print(f"{color('RED')}Nenhuma seleção oficial disponível para {selected_nation}.{color('RESET')}")
                time.sleep(2)
                self.start_selection()
                return

            print(f"{color('GOLDEN')}PROPOSTAS DISPONÍVEIS - {selected_nation.upper()}:{color('RESET')}\n")

            for i, team in enumerate(teams, 1):
                # Cálculo de preço baseado no overall_rating médio da seleção
                avg_rating = teams_df[teams_df[col_clube] == team][col_rating].mean()
                price = (avg_rating * 1000000) # Ex: 80 rating = 80 Milhões
                
                status_color = color('GREEN') if balance >= price else color('RED')
                print(f" [{i}] {team:<30} | ⭐ Rating: {avg_rating:.1f} | {status_color}Custo: ${price:,.2f}{color('RESET')}")

            choice = input(f"\n{color('MAGENTA')}Deseja comprar esta federação? (0 para voltar): {color('RESET')}")
            
            if choice != '0':
                chosen_team = teams[int(choice)-1]
                update_json('current_club', chosen_team)
                print(f"\n{color('GREEN')}🖋️  PARABÉNS! VOCÊ É O NOVO PRESIDENTE DA FEDERAÇÃO: {chosen_team.upper()}{color('RESET')}")
                time.sleep(3)

        except Exception as e:
            print(f"\n{color('RED')}❌ Erro no Seletor: {e}{color('RESET')}")
            time.sleep(5)