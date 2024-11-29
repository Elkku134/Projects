import pyautogui
import time
import random

how_long = 2  #in hours
how_long = int(how_long)
time_seconds = how_long*60*60
#time_seconds=7200
time_seconds= int(time_seconds/10)

for i in range(time_seconds):
    x = random.randint(900, 910)
    y = random.randint(500, 510)
    pyautogui.moveTo(x,y,0.5)
    pyautogui.click(x, y)
    gone = round(i/6, 2)
    left = round((time_seconds-gone*10)/6, 2)
    print("X-coordinate location:", x, "Y-coordinate location:", y, "Minutes gone", gone, "Minutes left", left)
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
    
    


