import pyautogui
import random

X_BELLOSOM = 1021
Y_BELLOSOM = 526
RGB_BELLOSOM = (97, 140, 100)

USE_POKEBALL = True

POKE_DEAD_POSITION = (1036, 594) 
BP_LOOT_POSITION = (1703, 840)

LIST_ATTACK_ROSE = ['f9', 'f10', 'f7', 'f6', 'f4', 'f5', 'f8', 'f1', 'f2', 'f3']
LIST_OCEAN_POSITION = [(821, 442), (944, 320)]

BATTLE_REGION = (1151, 383, 204, 162)

TARGET_X = 1776
TARGET_Y = 390


def check_battle():
    battle = pyautogui.locateOnScreen('batalha.PNG', confidence=0.8, region=BATTLE_REGION)
    if battle is not None:
        return True
    return False

def click_fish(x_fish, y_fish):
    pyautogui.moveTo(x_fish, y_fish)
    pyautogui.click()

def poke_atack():
    pyautogui.press(LIST_ATTACK_ROSE)

def get_loot():
    pyautogui.moveTo(POKE_DEAD_POSITION)
    pyautogui.click(button='right')
    pyautogui.sleep(0.8)
    pyautogui.moveTo(BP_LOOT_POSITION)
    pyautogui.click(clicks=5)

def use_pokeball():
    if USE_POKEBALL:
        pyautogui.moveTo(POKE_DEAD_POSITION)
        pyautogui.press('capslock')
        pyautogui.sleep(0.8)
        pyautogui.click()


def check_poke_position():
    poke = pyautogui.pixelMatchesColor(X_BELLOSOM, Y_BELLOSOM, RGB_BELLOSOM)
    if not poke:
        pyautogui.press('q')
        pyautogui.sleep(0.8)
        pyautogui.moveTo(X_BELLOSOM, Y_BELLOSOM)
        pyautogui.click()

def use_fishing_rod():
    ocean_position = random.choice(LIST_OCEAN_POSITION)
    pyautogui.press('delete')
    pyautogui.moveTo(ocean_position)
    pyautogui.click()

def attack_target(TARGET_X, TARGET_Y):
    pyautogui.moveTo(TARGET_X, TARGET_Y) #função mover o mouse para as coordenadas x e y
    pyautogui.sleep(0.4)
    pyautogui.click() #função clicar com o mouse na posição atual

