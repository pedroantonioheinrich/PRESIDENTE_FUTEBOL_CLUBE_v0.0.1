import os
import json
from SRC.USER_INTERFACE.UTILS.utils_color_pallete import ColorPallete


color_choice = ColorPallete()
color = color_choice.color_picker

def save_json(usr_data):
    # Certificando-se de que a pasta SAVES existe
    os.makedirs(os.path.dirname('SAVES/user_data.json'), exist_ok=True)
    # 💾 Gravando as informações
    with open('SAVES/user_data.json', "w", encoding="utf-8") as file:
        # indent=4 deixa o arquivo legível para humanos
        # ensure_ascii=False permite acentos (como o 'ã' de brasileiro)
        json.dump(usr_data, file, indent=4, ensure_ascii=False)
        print(f"{color('CYAN')} Configurações salvas com sucesso!! {color('RESET')}")


def read_json(dir, usr_data):
    try:
        with open(f"{dir}/{usr_data}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except:
        print(f"{color('RED')} Arquivo não encontrado! O usuário ainda não se registrou. {color('RESET')}")
        print("")
        return None


def update_json(new_key, new_value):
    file_path = 'SAVES/user_data.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding="utf-8")  as file:
            actual_data = json.load(file)
    else:
        actual_data = {}

    actual_data[new_key] = new_value

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(actual_data, file, indent=4, ensure_ascii=False)
        print(f"{color('GREEN')} ✅ Dados atualizados: {new_key}: {new_value} ADICIONADO! {color('RESET')}")