import pyautogui
import time
import random

time_seconds=7200
time_seconds= int(time_seconds/10)

for i in range(time_seconds):
    x = random.randint(900, 1000)
    y = random.randint(500, 600)
    pyautogui.moveTo(x,y,0.5)
    pyautogui.click(x, y)
    print(x, y, "Seconds gone", i*10)
    time.sleep(10)








"""
while True:
    x = random.randint(900, 1000)
    y = random.randint(500, 600)
    pyautogui.moveTo(x,y,0.5)
    pyautogui.click(x, y)
    print(x, y)
    time.sleep(5)
"""   
    
    


