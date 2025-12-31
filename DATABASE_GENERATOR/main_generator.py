import FreeSimpleGUI as sg
import csv
import os
from db_manager import DBManager

CSV_FILE = 'DATABASE_GENERATOR/temp_database.csv'

def save_to_csv(data):
    os.makedirs('DATABASE_GENERATOR', exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)
    
    # Cabeçalhos expandidos para suportar todos os Extras
    headers = ['Tipo', 'Nome', 'Nacao', 'Atributo_Principal', 
               'Extra_1', 'Extra_2', 'Extra_3', 'Extra_4', 'Extra_5', 'Extra_6']
    
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def create_generator_ui():
    sg.theme('DarkBlue3')

    # --- LAYOUTS ---
    layout_clube = [
        [sg.Text('IDENTIFICAÇÃO', font=('Helvetica', 10, 'bold'), text_color='gold')],
        [sg.Text('Nome Oficial:', size=(15, 1)), sg.Input(key='-C_NAME-', expand_x=True)],
        [sg.Text('Apelido/Sigla:', size=(15, 1)), sg.Input(key='-C_NICKNAME-', size=(10, 1)), sg.Text('Fundação (Ano):'), sg.Input(key='-C_FOUNDED-', size=(6, 1))],
        [sg.Text('País:', size=(15, 1)), sg.Input(key='-C_NATION-', expand_x=True)],
        [sg.Text('Divisão:', size=(15, 1)), sg.Combo(['Série A', 'Série B', 'Série C', 'Nacional'], default_value='Série A', key='-C_DIVISION-')],
        [sg.HSeparator()],
        [sg.Text('INFRAESTRUTURA E TORCIDA', font=('Helvetica', 10, 'bold'), text_color='gold')],
        [sg.Text('Estádio:', size=(15, 1)), sg.Input(key='-C_STADIUM-', expand_x=True)],
        [sg.Text('Capacidade:', size=(15, 1)), sg.Input(key='-C_CAPACITY-', size=(10, 1)), sg.Text('Fiel Torcida (1-100):'), sg.Slider(range=(1, 100), orientation='h', key='-C_FAN_LOYALTY-')],
        [sg.Text('Nível CT:', size=(15, 1)), sg.Slider(range=(1, 10), orientation='h', key='-C_TRAINING_LVL-')],
        [sg.HSeparator()],
        [sg.Text('FINANCEIRO E STATUS', font=('Helvetica', 10, 'bold'), text_color='gold')],
        [sg.Text('Orçamento Inicial:', size=(15, 1)), sg.Input(key='-C_BUDGET-', size=(20, 1))],
        [sg.Text('Reputação Atual:', size=(15, 1)), sg.Slider(range=(1, 100), orientation='h', default_value=50, key='-C_REP-')],
    ]

    layout_jogador = [
        [sg.Text('DADOS BÁSICOS', font=('Helvetica', 10, 'bold'), text_color='cyan')],
        [sg.Text('Nome Completo:', size=(15, 1)), sg.Input(key='-P_NAME-', expand_x=True)],
        [sg.Text('Nacionalidade:', size=(15, 1)), sg.Input(key='-P_NATION-', size=(20, 1)), sg.Text('Idade:'), sg.Spin([i for i in range(15, 50)], initial_value=20, key='-P_AGE-')],
        [sg.Text('Posição:', size=(15, 1)), sg.Combo(['GOL', 'ZAG', 'LAT', 'VOL', 'MEI', 'ATA'], key='-P_POS-')],
        [sg.HSeparator()],
        [sg.Text('ATRIBUTOS TÉCNICOS', font=('Helvetica', 10, 'bold'), text_color='cyan')],
        [sg.Text('Velocidade:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', default_value=50, key='-P_SPEED-', enable_events=True)],
        [sg.Text('Técnica/Passe:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', default_value=50, key='-P_SKILL-', enable_events=True)],
        [sg.Text('Finalização:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', default_value=50, key='-P_FINISH-', enable_events=True)],
        [sg.Text('Defesa/Físico:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', default_value=50, key='-P_DEFENSE-', enable_events=True)],
        [sg.Frame('Resultado Final', [[
            sg.Text('OVERALL CALCULADO:', font=('Helvetica', 12, 'bold')),
            sg.Text('50', key='-P_OVERALL_DISPLAY-', font=('Helvetica', 20, 'bold'), text_color='yellow'),
            sg.Text('Potencial:'), sg.Slider(range=(1, 99), orientation='h', default_value=75, key='-P_POTENTIAL-')
        ]], element_justification='center', expand_x=True)],
        [sg.HSeparator()],
        [sg.Text('FINANCEIRO', font=('Helvetica', 10, 'bold'), text_color='cyan')],
        [sg.Text('Salário ($):', size=(12, 1)), sg.Input(key='-P_WAGE-', size=(15, 1)), sg.Text('Valor Passe:'), sg.Input(key='-P_MARKET_VAL-', size=(15, 1)), sg.Text('Pé:'), sg.Combo(['Destro', 'Canhoto'], key='-P_FOOT-')]
    ]

    layout_tecnico = [
        [sg.Text('PERFIL DO TÉCNICO', font=('Helvetica', 10, 'bold'), text_color='orange')],
        [sg.Text('Nome:', size=(15, 1)), sg.Input(key='-T_NAME-', expand_x=True)],
        [sg.Text('País:', size=(15, 1)), sg.Input(key='-T_NATION-', size=(20, 1)), sg.Text('Idade:'), sg.Spin([i for i in range(30, 85)], initial_value=45, key='-T_AGE-')],
        [sg.Text('Estilo:', size=(15, 1)), sg.Combo(['Ofensivo', 'Defensivo', 'Posse'], key='-T_STYLE-'), sg.Text('Formação:'), sg.Input(key='-T_FORMATION-', size=(10, 1))],
        [sg.Text('Liderança:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', key='-T_LEADERSHIP-')],
        [sg.Text('Tática:', size=(15, 1)), sg.Slider(range=(1, 99), orientation='h', key='-T_TACTIC-')],
        [sg.Text('Salário:', size=(15, 1)), sg.Input(key='-T_WAGE-', size=(15, 1)), sg.Text('Reputação:'), sg.Slider(range=(1, 99), orientation='h', key='-T_REP-')]
    ]

    layout_juiz = [
        [sg.Text('Nome:'), sg.Input(key='-J_NAME-')],
        [sg.Text('Federação:'), sg.Input(key='-J_NATION-')],
        [sg.Text('Rigor (1-10):'), sg.Slider(range=(1, 10), orientation='h', key='-J_RIGOR-')]
    ]

    layout_comp = [
        [sg.Text('Nome:'), sg.Input(key='-COMP_NAME-')],
        [sg.Text('Tipo:'), sg.Combo(['Liga', 'Copa', 'Continental'], key='-COMP_TYPE-')],
        [sg.Text('Premiação:'), sg.Input(key='-COMP_PRIZE-')],
        [sg.Text('Times:'), sg.Spin([i for i in range(2, 40)], key='-COMP_TEAMS-')],
        [sg.Text('Turnos:'), sg.Radio('1', "T", key='-COMP_T1-'), sg.Radio('2', "T", default=True, key='-COMP_T2-')],
        [sg.Text('Vagas Int:'), sg.Input(key='-COMP_VAGAS-', size=(5, 1)), sg.Text('Rebaixamento:'), sg.Input(key='-COMP_REB-', size=(5, 1))],
        [sg.Text('Prestígio:'), sg.Slider(range=(1, 10), orientation='h', key='-COMP_LEVEL-')]
    ]

    # --- ESTRUTURA PRINCIPAL ---
    layout = [
        [sg.Text('⚽ PRESIDENTE FC - DATABASE MANAGER', font=('Helvetica', 20, 'bold'), text_color='#FFD700')],
        [sg.TabGroup([[
            sg.Tab('Clube', layout_clube),
                        sg.Tab('Jogador', layout_jogador),
            sg.Tab('Técnico', layout_tecnico),
            sg.Tab('Juiz', layout_juiz),
            sg.Tab('Competição', layout_comp)
        ]], key='-TABS-')],
        [sg.Button('💾 SALVAR NO CSV', key='Salvar no CSV', size=(20, 2)), 
         sg.Button('⚙️ GERAR SQLITE', key='Gerar Banco SQLite', size=(20, 2)),
         sg.Button('🚪 SAIR', key='Sair', size=(10, 2))]
    ]

    window = sg.Window('Presidente FC v1.0', layout, finalize=True, element_justification='center')

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Sair'):
            break

        # Lógica de Cálculo de Overall
        if event in ('-P_SPEED-', '-P_SKILL-', '-P_FINISH-', '-P_DEFENSE-', '-P_POS-'):
            try:
                v = int(values['-P_SPEED-'])
                t = int(values['-P_SKILL-'])
                f = int(values['-P_FINISH-'])
                d = int(values['-P_DEFENSE-'])
                pos = values['-P_POS-']

                if pos == 'ATA':
                    ovr = (v*0.2 + t*0.2 + f*0.5 + d*0.1)
                elif pos in ['ZAG', 'VOL']:
                    ovr = (v*0.1 + t*0.2 + f*0.1 + d*0.6)
                elif pos == 'MEI':
                    ovr = (v*0.1 + t*0.6 + f*0.2 + d*0.1)
                elif pos == 'GOL':
                    ovr = (d*0.8 + t*0.2)
                else:
                    ovr = (v + t + f + d) / 4

                window['-P_OVERALL_DISPLAY-'].update(int(ovr))
            except Exception:
                pass

        # Salvamento no CSV
        if event == 'Salvar no CSV':
            tab_ativa = values['-TABS-']
            dados = {'Tipo': tab_ativa}
            
            try:
                if tab_ativa == 'Clube':
                    dados.update({
                        'Nome': values['-C_NAME-'],
                        'Nacao': values['-C_NATION-'],
                        'Atributo_Principal': values['-C_BUDGET-'],
                        'Extra_1': values['-C_REP-'],
                        'Extra_2': values['-C_DIVISION-'],
                        'Extra_3': values['-C_STADIUM-'],
                        'Extra_4': values['-C_CAPACITY-'],
                        'Extra_5': values['-C_TRAINING_LVL-'],
                        'Extra_6': values['-C_NICKNAME-']
                    })
                elif tab_ativa == 'Jogador':
                    dados.update({
                        'Nome': values['-P_NAME-'],
                        'Nacao': values['-P_NATION-'],
                        'Atributo_Principal': window['-P_OVERALL_DISPLAY-'].get(),
                        'Extra_1': values['-P_POS-'],
                        'Extra_2': values['-P_AGE-'],
                        'Extra_3': values['-P_POTENTIAL-'],
                        'Extra_4': values['-P_WAGE-'],
                        'Extra_5': values['-P_MARKET_VAL-'],
                        'Extra_6': values['-P_FOOT-']
                    })
                elif tab_ativa == 'Técnico':
                    dados.update({
                        'Nome': values['-T_NAME-'],
                        'Nacao': values['-T_NATION-'],
                        'Atributo_Principal': values['-T_REP-'],
                        'Extra_1': values['-T_STYLE-'],
                        'Extra_2': values['-T_FORMATION-'],
                        'Extra_3': values['-T_LEADERSHIP-'],
                        'Extra_4': values['-T_TACTIC-'],
                        'Extra_5': values['-T_WAGE-'],
                        'Extra_6': values['-T_AGE-']
                    })
                elif tab_ativa == 'Juiz':
                    dados.update({
                        'Nome': values['-J_NAME-'],
                        'Nacao': values['-J_NATION-'],
                        'Atributo_Principal': values['-J_RIGOR-']
                    })
                elif tab_ativa == 'Competição':
                    t = '1' if values['-COMP_T1-'] else '2'
                    dados.update({
                        'Nome': values['-COMP_NAME-'],
                        'Nacao': 'N/A',
                        'Atributo_Principal': values['-COMP_TYPE-'],
                        'Extra_1': values['-COMP_PRIZE-'],
                        'Extra_2': values['-COMP_TEAMS-'],
                        'Extra_3': t,
                        'Extra_4': values['-COMP_VAGAS-'],
                        'Extra_5': values['-COMP_REB-'],
                        'Extra_6': values['-COMP_LEVEL-']
                    })

                save_to_csv(dados)
                sg.popup(f'✅ {tab_ativa} salvo com sucesso!')
            except Exception as e:
                sg.popup_error(f'Erro ao salvar: {e}')

        # Geração do Banco SQLite
        if event == 'Gerar Banco SQLite':
            if os.path.exists(CSV_FILE):
                manager = DBManager()
                sucesso, msg = manager.process_temp_csv(CSV_FILE)
                sg.popup('Resultado', msg)
            else:
                sg.popup_error('CSV não encontrado!')

    window.close()

if __name__ == '__main__':
    create_generator_ui()
