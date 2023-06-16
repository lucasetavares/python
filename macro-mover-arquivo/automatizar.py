import pyautogui
import time

# Passo a passo para organizar uma automação:
pyautogui.alert("O código vai começar. Tire a mão do teclado e do mouse!")
pyautogui.PAUSE = 0.5
# 1º - abrir o google drive
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
pyautogui.moveTo(1074, 619)
pyautogui.click()
pyautogui.moveTo(409, 68)
pyautogui.click()
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.moveTo(851, 104)
pyautogui.click()

# 2º - entrar na minha área de trabalho
pyautogui.hotkey('winleft', 'd')
time.sleep(0.5)
# 3º - cliquei no arquivo que eu quero fazer backup e arrastei ele
pyautogui.moveTo(1577, 302)
time.sleep(0.5)
pyautogui.mouseDown()
time.sleep(0.5)
pyautogui.moveTo(1212, 947)
# 4º - enquanto eu to arrastando, eu vou mudar para o google drive
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
# 5º - larguei o arquivo no google drive
pyautogui.mouseUp()
# 6º - esperar 5 segundos
time.sleep(5)
pyautogui.alert("O código acabou de rodar. Pode usar o computador novamente.")

