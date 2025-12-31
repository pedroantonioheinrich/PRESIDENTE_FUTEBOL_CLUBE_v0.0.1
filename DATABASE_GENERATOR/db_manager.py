import sqlite3
import pandas as pd
import os

class DBManager:
    def __init__(self, db_name='DATA/presidente_fc.db'):
        # Garante que a pasta DATA exista na raiz do projeto
        if not os.path.exists('DATA'):
            os.makedirs('DATA')
            
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Cria a estrutura completa de tabelas para o simulador"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')

        # 1. TABELA DE PAÍSES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS paises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT UNIQUE NOT NULL
            )
        ''')

        # 2. TABELA DE CLUBES (Com infraestrutura e finanças)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clubes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                apelido TEXT,
                pais_id INTEGER,
                divisao TEXT,
                estadio TEXT,
                capacidade INTEGER,
                nivel_ct INTEGER,
                reputacao INTEGER,
                orcamento REAL,
                fiel_torcida INTEGER,
                FOREIGN KEY (pais_id) REFERENCES paises (id)
            )
        ''')

        # 3. TABELA DE JOGADORES (Com atributos técnicos e contrato)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jogadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nacionalidade TEXT,
                idade INTEGER,
                posicao TEXT,
                pe_dominante TEXT,
                overall INTEGER,
                potencial INTEGER,
                salario REAL,
                valor_mercado REAL,
                clube_id INTEGER,
                FOREIGN KEY (clube_id) REFERENCES clubes (id)
            )
        ''')

        # 4. TABELA DE TÉCNICOS
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tecnicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                nacionalidade TEXT,
                idade INTEGER,
                estilo_jogo TEXT,
                formacao_pref TEXT,
                lideranca INTEGER,
                tatica INTEGER,
                reputacao INTEGER,
                salario REAL
            )
        ''')

        # 5. TABELA DE COMPETIÇÕES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS competicoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT,
                num_clubes INTEGER,
                turnos INTEGER,
                vagas_libertadores INTEGER,
                rebaixamento INTEGER,
                premiacao REAL,
                cota_tv REAL,
                prestigio INTEGER
            )
        ''')

        # 6. TABELA DE JUÍZES
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS juizes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                federacao TEXT,
                rigor INTEGER
            )
        ''')

        conn.commit()
        conn.close()

    def process_temp_csv(self, csv_path):
        """Converte os dados do CSV para as tabelas específicas do SQLite"""
        try:
            if not os.path.exists(csv_path):
                return False, "Arquivo CSV não encontrado."

            df = pd.read_csv(csv_path)
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            for _, row in df.iterrows():
                tipo = row['Tipo']
                
                # Tratamento de Países (Global para quase todos)
                if str(row['Nacao']) != 'nan' and str(row['Nacao']) != 'N/A':
                    cursor.execute("INSERT OR IGNORE INTO paises (nome) VALUES (?)", (row['Nacao'],))
                    cursor.execute("SELECT id FROM paises WHERE nome = ?", (row['Nacao'],))
                    pais_id = cursor.fetchone()[0]
                else:
                    pais_id = None

                if tipo == 'Clube':
                    cursor.execute('''
                        INSERT INTO clubes (nome, apelido, pais_id, orcamento, reputacao, divisao, estadio, capacidade, nivel_ct)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (row['Nome'], row['Extra_6'], pais_id, row['Atributo_Principal'], row['Extra_1'], 
                          row['Extra_2'], row['Extra_3'], row['Extra_4'], row['Extra_5']))

                elif tipo == 'Jogador':
                    # Tenta associar ao clube pelo nome se estiver no Extra_6 do cadastro de jogador
                    # Caso contrário, deixa o vínculo para depois
                    cursor.execute("""
                        INSERT INTO jogadores (nome, nacionalidade, overall, posicao, idade, potencial, salario, valor_mercado, pe_dominante) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (row['Nome'], row['Nacao'], row['Atributo_Principal'], row['Extra_1'], 
                          row['Extra_2'], row['Extra_3'], row['Extra_4'], row['Extra_5'], row['Extra_6']))

                elif tipo == 'Técnico':
                    cursor.execute('''
                        INSERT INTO tecnicos (nome, nacionalidade, reputacao, estilo_jogo, formacao_pref, lideranca, tatica, salario, idade)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (row['Nome'], row['Nacao'], row['Atributo_Principal'], row['Extra_1'], 
                          row['Extra_2'], row['Extra_3'], row['Extra_4'], row['Extra_5'], row['Extra_6']))

                elif tipo == 'Competição':
                    cursor.execute('''
                        INSERT INTO competicoes (nome, tipo, premiacao, num_clubes, turnos, vagas_libertadores, rebaixamento, prestigio)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (row['Nome'], row['Atributo_Principal'], row['Extra_1'], row['Extra_2'], 
                          row['Extra_3'], row['Extra_4'], row['Extra_5'], row['Extra_6']))

                elif tipo == 'Juiz':
                    cursor.execute('''
                        INSERT INTO juizes (nome, federacao, rigor)
                        VALUES (?, ?, ?)
                    ''', (row['Nome'], row['Nacao'], row['Atributo_Principal']))

            conn.commit()
            conn.close()
            return True, "Banco de Dados atualizado com sucesso!"
            
        except Exception as e:
            return False, f"Erro ao processar: {str(e)}"