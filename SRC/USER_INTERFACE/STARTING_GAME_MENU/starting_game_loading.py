import sys
import random
import time
import SRC.USER_INTERFACE.UTILS.utils  as utils 
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete
from game_version import VERSION





def loading_screen():

    color_choice = ColorPallete()
    color = color_choice.color_picker

    phrases = [
        "🌱 Aparando a grama do estádio...",
        "⚽ Inflando as bolas de treino...",
        "🖥️ Calibrando o VAR (pode demorar)...",
        "🤫 Subornando... digo, negociando com empresários...",
        "🪑 Esquentando o banco de reservas...",
        "📋 Desenhando táticas no quadro negro...",
        "👕 Lavando os uniformes para o jogo...",
        "💰 Contando as moedas na tesouraria...",
        "🏃 Expulsando gandulas invasores...",
        "💵 Sincronizando o bicho dos jogadores...",
        "☕ Preparando o café do Presidente...",
        "🍺 Aumentando o preço da cerveja na Arena...",
        "🎯 Treinando a pontaria do centroavante...",
        "💡 Ajustando o brilho dos refletores...",
        "📑 Ocultando dívidas do balanço mensal...",
        "👳 Pedindo aporte para o Magnata Árabe..."
    ]

    width_bar = 40
    total_steps = 100
    actual_phrase = random.choice(phrases)
    
    utils.clear_screen()
    
    print("\n" * 5)
    print(f"{color("CYAN")}{color("RESET")}" + f" PRESIDENTE FUTEBOL CLUBE {VERSION} ".center(60, "═") + f"{color("RESET")}")
    print("\n")

    for i in range(total_steps + 1):
        # Atualiza a frase a cada 12 passos para dar tempo de leitura
        if i % 12 == 0:
            actual_phrase = random.choice(phrases)

        # Desenho da barra
        progress = int((i / total_steps) * width_bar)
        bar = "█" * progress + "░" * (width_bar - progress)
        percentual = f"{i}%"
        
        # O SEGREDO: Usamos \033[A para subir uma linha, limpamos com \r e imprimimos as duas
        # Isso garante que a frase e a barra ocupem sempre o mesmo espaço
        sys.stdout.write("\r" + " " * 70 + "\r") # Limpa a linha da frase
        sys.stdout.write(f"  {color("YELLOW")}{actual_phrase}{color("RESET")}\n")
        sys.stdout.write(f"\r  {color("GREEN")}[{bar}] {percentual}{color("RESET")}")
        
        # Movemos o cursor de volta para cima para a próxima iteração
        sys.stdout.write("\033[A") 
        sys.stdout.flush()
        
        # Velocidade variável
        time.sleep(random.uniform(0.02, 0.1))

    # Finalização para não sobrescrever a última linha
    sys.stdout.write("\n\n")
    print(f"{color("GREEN")}  SISTEMA PRONTO! ENTRANDO NO GABINETE...{color("RESET")}")
    time.sleep(1.2)
    utils.clear_screen()

if __name__ == "__main__":
    loading_screen()