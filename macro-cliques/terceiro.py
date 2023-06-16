import threading
import keyboard
import autoit
import pyautogui
from pynput import keyboard as kb

# Coordenadas originais do cursor
original_x = 964
original_y = 536

# Função para executar o clique
def executar_clique():
    x_destino = 1814
    y_destino = 400
    autoit.mouse_click("left", x_destino, y_destino, 1, 0)
    pyautogui.moveTo(original_x, original_y)

# Função para executar os cliques
def executar_cliques():
    coordenadas = [
        (964, 536),  # Coordenada 1
        (1703, 843)  # Coordenada 2
    ]
    for i, (x, y) in enumerate(coordenadas):
        if i == 0:
            autoit.mouse_click("right", x, y, 1, 0)  # Clique único na primeira coordenada
        elif i == 1:
            autoit.mouse_click("right", x, y, 5, 0)  # Clique cinco vezes na segunda coordenada
        pyautogui.sleep(0.15)
        pyautogui.moveTo(original_x, original_y)

# Função para executar o clique quando a tecla "R" é pressionada
def executar_clique_r():
    pyautogui.press(ATTACK_AMOONGUS)

# Função chamada ao pressionar a tecla "F"
def on_press_F(event):
    if event.event_type == keyboard.KEY_DOWN:
        executar_cliques()

# Função para encerrar o programa
def encerrar_programa():
    keyboard.unhook_all()
    keyboard.clear_all_hotkeys()

# Criação dos objetos de combinação de teclas
combinations = [
    {kb.KeyCode.from_char('r')},
    {kb.KeyCode.from_char('R')},
]

# Conjunto de teclas pressionadas atualmente
current_keys = set()
ATTACK_AMOONGUS = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']

# Função chamada ao pressionar uma tecla
def on_press(key):
    if any(key in combo for combo in combinations):
        current_keys.add(key)
        if all(k in current_keys for k in combinations[0]) or all(k in current_keys for k in combinations[1]):
            executar_clique_r()

# Função chamada ao soltar uma tecla
def on_release(key):
    if any(key in combo for combo in combinations):
        current_keys.remove(key)

# Função para iniciar o monitoramento das teclas
def monitorar_teclas():
    with kb.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Função principal para executar o código do clique
def executar_clicar():
    keyboard.add_hotkey('3', executar_clique)
    keyboard.wait('esc')

# Criação das threads para executar as funcionalidades
thread_monitorar_teclas = threading.Thread(target=monitorar_teclas)
thread_executar_clicar = threading.Thread(target=executar_clicar)

# Inicia as threads
thread_monitorar_teclas.start()
thread_executar_clicar.start()

# Adiciona o "hook" para capturar o pressionamento da tecla "F"
keyboard.on_press_key("F", on_press_F)

# Mantém o programa em execução
keyboard.wait("esc")
