import pyautogui
import time
import random


while True:
    x = random.randint(900, 1000)
    y = random.randint(500, 600)
    pyautogui.moveTo(x,y,0.5)
    pyautogui.click(x, y)
    print(x, y)
    time.sleep()
    



