# pip install pyautogui keyboard — установка библиотек
import pyautogui
import keyboard
from time import sleep


while True:
    if keyboard.is_pressed('ctrl+shift'):
        for i in range(3, 0, -1):
            print(f'Начинаю работу через {i} секунды')
            sleep(1)

        while 1:
            pyautogui.click()
            if keyboard.is_pressed('esc'):
                print('Работа завершена!')
                break
    else:
        keyboard.wait('ctrl+shift')