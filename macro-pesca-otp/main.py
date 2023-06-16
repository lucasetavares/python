import pyautogui

from actions import check_battle, check_poke_position, click_fish, get_loot, poke_atack, use_fishing_rod, use_pokeball, attack_target


X_FISH = 764
Y_FISH = 562
RGB_FISH = (67, 165, 52)

TARGET_X = 1776
TARGET_Y = 390

MAX_ATTEMPT = 750
attempt = 0

while True:
    fish = pyautogui.pixelMatchesColor(X_FISH, Y_FISH, RGB_FISH)
    attempt = attempt + 1
    print(attempt)
    if fish:
        click_fish(X_FISH, Y_FISH)
        pyautogui.sleep(1.5)
        if not check_battle():
            attack_target(TARGET_X, TARGET_Y)
            poke_atack()
        poke_atack()
        pyautogui.sleep(1.5)
        get_loot()
        use_pokeball()
        check_poke_position()
        pyautogui.sleep(2.5)
        check_poke_position()
        poke_atack()
        use_fishing_rod()
        attempt = 0
    if attempt == MAX_ATTEMPT:
        use_fishing_rod()
        attempt = 0