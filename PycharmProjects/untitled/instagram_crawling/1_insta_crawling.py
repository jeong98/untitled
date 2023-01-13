import time
import pyautogui
import datetime
import os
import configparser as parser

properties = parser.ConfigParser()

path = os.getcwd()
properties.read(path + '/config.ini')
user_id = properties['ETC']['user']
scroll_cnt = int(properties['ETC']['scroll_cnt'])

today = datetime.datetime.today()
file_name = f'{today.year}_{today.month}_{today.day}'
properties.set('ETC', 'date', file_name)

with open(path + '/config.ini','w') as configfile:
    properties.write(configfile)

F = [f"https://www.instagram.com/{user_id}/followers/", f"https://www.instagram.com/{user_id}/following/"]
for idx, i in enumerate(F):
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write('chrome')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write(i)
    time.sleep(1)
    pyautogui.press('enter')

    win = pyautogui.getWindowsWithTitle('Chrome')[0]
    W, H = win.width, win.height
    pyautogui.moveTo(win.left+W // 2, win.top+H // 2)
    time.sleep(5)
    c = 0
    while c < scroll_cnt:
        pyautogui.scroll(-3000)
        time.sleep(1)
        c += 1
    pyautogui.hotkey('ctrl', 's')
    time.sleep(5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('end')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.hotkey('shift', 'tab')
    time.sleep(0.5)
    pyautogui.write(f'{file_name}_{["followers","following"][idx]}')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)

    pyautogui.write(path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
