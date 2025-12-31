import pandas as pd
import os

def test_csv_structure():
    csv_path = 'DATA/data_fifa_players_database.csv'
    
    # Verifica se o arquivo existe antes de abrir
    if not os.path.exists(csv_path):
        print(f"❌ Erro: O arquivo {csv_path} não foi encontrado!")
        return

    try:
        # Carrega apenas as primeiras 5 linhas para ser rápido
        df = pd.read_csv(csv_path, nrows=5)
        
        print("\n" + "="*50)
        print("🔍 INSPEÇÃO DE ESTRUTURA DO CSV")
        print("="*50)
        
        # 1. Lista todas as colunas disponíveis
        print(f"\n✅ Colunas encontradas ({len(df.columns)}):")
        for col in df.columns:
            print(f" - {col}")
        
        print("\n" + "="*50)
        
        # 2. Sugestão de mapeamento
        # Vamos tentar adivinhar quais colunas você deve usar no código
        posiveis_paises = [c for c in df.columns if c in ['Nationality', 'Nation', 'Country', 'country_name']]
        posiveis_clubes = [c for c in df.columns if c in ['Club', 'Team', 'club_name', 'team_name']]
        posiveis_overall = [c for c in df.columns if c in ['Overall', 'rating', 'overall_rating']]

        print("📋 SUGESTÃO DE MAPEAMENTO PARA O SEU CÓDIGO:")
        print(f" > Coluna de País: {posiveis_paises[0] if posiveis_paises else 'NÃO ENCONTRADA'}")
        print(f" > Coluna de Clube: {posiveis_clubes[0] if posiveis_clubes else 'NÃO ENCONTRADA'}")
        print(f" > Coluna de Nível (Overall): {posiveis_overall[0] if posiveis_overall else 'NÃO ENCONTRADA'}")
        
        print("\n" + "="*50)
        print("📝 AMOSTRA DOS DADOS (Primeiras 3 linhas):")
        print(df.head(3))
        print("="*50)

    except Exception as e:
        print(f"❌ Ocorreu um erro ao ler o CSV: {e}")

if __name__ == "__main__":
    test_csv_structure()