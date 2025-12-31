import time
from SRC.USER_INTERFACE.UTILS.utils_json_update import update_json
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import color
from SRC.USER_INTERFACE.UTILS.utils import clear_screen


def show_personality_menu():

    clear_screen()

    # Cabeçalho de Personalidade
    print(f"{color('GOLD')}╔" + "═"*73 + "╗")
    print(f"║{color('RESET')}{color('BOLD')}  🧠 PERFIL PSICOLÓGICO & LIDERANÇA{' ':^38}{color('GOLD')}║")
    print(f"╠" + "═"*73 + "╣")
    print(f"║{color('RESET')}  {color('GOLD')}✨ PERSONALIDADE: {color('BOLD')}Como você será conhecido no vestiário?{color('RESET')}{' ':^15}{color('GOLD')}║")
    print(f"╚" + "═"*73 + f"╝{color('RESET')}")

    print(f"\n{color('BOLD')}Escolha o seu arquétipo de liderança:{color('RESET')}\n")
    
    # Opções com Emojis
    print(f"{color('GOLD')}[ 1 ]{color('RESET')} {color('BOLD')}O ESTRATEGISTA{color('RESET')} 🧠 (Focado em finanças e visão de longo prazo)")
    print(f"{color('GOLD')}[ 2 ]{color('RESET')} {color('GOLD')}O APAIXONADO{color('RESET')} 🔥 (Movido pela emoção e conexão com a torcida)")
    print(f"{color('GOLD')}[ 3 ]{color('RESET')} {color('BOLD')}O DITADOR{color('RESET')} 👔 (Poder absoluto, exige disciplina impecável)")
    print(f"{color('GOLD')}[ 4 ]{color('RESET')} {color('BOLD')}O PARCEIRO{color('RESET')} 🤝 (Próximo aos jogadores e focado no bem-estar)")

    print(f"\n{color('CYAN')}   " + "─" * 69 + f"{color('RESET')}")
    
    escolha = input(f"{color('BOLD')}Sua escolha (1-4): {color('RESET')}")
    
    # Mapeamento para o JSON
    profiles = {
        "1": "Strategist",
        "2": "Passionate",
        "3": "Dictator",
        "4": "Partner"
    }
    
    final_personality = profiles.get(escolha, "Strategist")
    
    # Agora basta usar sua função de update!
    update_json('personality', final_personality)
    time.sleep(1)
    clear_screen()