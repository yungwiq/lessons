# pip install pyautogui keyboard — установка библиотек
import pyautogui
import keyboard
from time import sleep


for i in range(3, 0, -1):
    print(f'Начинаю работу через {i} секунды')
    sleep(1)

while True:
    pyautogui.click()
    if keyboard.is_pressed('esc'):
        print('Работа завершена!')
        break