import pyautogui
import keyboard
from datetime import datetime


while True:
    #print(pyautogui.position())
    print(pyautogui.locateOnScreen('battle.PNG', confidence=0.9))