from pynput import keyboard
import pyautogui

COMBINATIONS = [
    {keyboard.KeyCode(char='r')},
    {keyboard.KeyCode(char='R')},
    ]

ATTACK_AMOONGUS = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10']
current = set()

def execute():
    pyautogui.press(ATTACK_AMOONGUS)

def on_press(key):
    if any ([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
